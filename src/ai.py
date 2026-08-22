# src/ai.py
import math
import random
import threading
import numpy as np
from globals import *
from .board import Board

class AI:
    def __init__(self, board:Board):
        self.board = board
        self.screen = board.screen
        self.player = "AI"
        self.player_id = 1
        self.processing = False
        self.move_ready = False
        self.best_move = None

    def drawPieces(self, col, row):
        if self.player == "Human":
            self.screen.blit(x_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))
        elif self.player == "AI":
            self.screen.blit(o_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))

    def minmax(self, grid, depth, player_id, alpha=-np.inf, beta=np.inf):
        score = self.board.evaluate(grid, depth)

        if abs(score) == 10 or depth == 0:
            return score

        if player_id == -1:
            best_score = np.inf
            for [r, c] in self.board.empty_cells():
                grid[r][c] = -1
                best_score = min(best_score, self.minmax(grid, depth - 1, -player_id, alpha, beta))
                grid[r][c] = 0
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = -np.inf
            for [r, c] in self.board.empty_cells():
                grid[r][c] = 1
                best_score = max(best_score, self.minmax(grid, depth - 1, -player_id, alpha, beta))
                grid[r][c] = 0
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score

    def start_thinking(self):
        self.processing = True
        self.move_ready = False
        self.best_move = None
        thread = threading.Thread(target=self.calculate_move)
        thread.daemon = True
        thread.start()

    def calculate_move(self):
        depth = len(self.board.empty_cells())

        if depth == 0 or self.board.is_terminal_node(self.board.grid):
            self.processing = False
            return

        if depth == 9:
            self.best_move = random.choice(self.board.empty_cells())
        else:
            best_score = -np.inf
            best_move = None
            alpha = -np.inf
            beta = np.inf

            for [r, c] in self.board.empty_cells():
                self.board.grid[r][c] = 1
                score = self.minmax(self.board.grid, depth - 1, -self.player_id, alpha, beta)
                self.board.grid[r][c] = 0 
                
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
                
                alpha = max(alpha, best_score)

            self.best_move = best_move

        self.move_ready = True

    def apply_move(self):
        if self.best_move:
            r, c = self.best_move
            self.board.grid[r][c] = 1
            self.drawPieces(c, r)
            self.board.moves_count += 1

        self.processing = False
        self.move_ready = False

        if self.board.verify_check(self.board.grid, 1):
            self.board.gameFinished = True
            self.board.winner = "AI"
        else:
            self.board.player = "Human"
            self.board.player_id = -1