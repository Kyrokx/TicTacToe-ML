import math
import random

import numpy as np

from globals import *
from .board import Board


class AI:
    def __init__(self, board:Board):
        self.board = board
        self.screen = board.screen
        self.player = "AI"
        self.player_id = 1
        

    def drawPieces(self, col, row):
        if self.player == "Human":
            self.screen.blit(x_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))

        elif self.player == "AI":
            self.screen.blit(o_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))

    def minmax(self, grid, depth, player_id):
        score = self.board.evaluate(grid, depth)

        if abs(score) == 10 or depth == 0:
            print(f"Returning score {score} at depth {depth}")
            return score

        if player_id == -1:  # It's human turn: We want to minimize
            best_score = np.inf
            for [r, c] in self.board.empty_cells():
                grid[r][c] = -1
                best_score = min(best_score, self.minmax(grid, depth - 1, -player_id))
                grid[r][c] = 0
            print(f"Best score for human: {best_score}")
            return best_score

        else:  # It's AI turn: We want to maximize
            best_score = -np.inf
            for [r, c] in self.board.empty_cells():
                grid[r][c] = 1
                best_score = max(best_score, self.minmax(grid, depth - 1, -player_id))
                grid[r][c] = 0
            print(f"Best score for AI: {best_score}")
            return best_score

    def play(self):
        r, c = 0, 0
        depth = len(self.board.empty_cells())

        if depth == 0 or self.board.is_terminal_node(self.board.grid):
            return

        if depth == 9:
            [r, c] = random.choice(self.board.empty_cells())

        else:
            best_score = -np.inf
            best_move = None

            for [r, c] in self.board.empty_cells():
                self.board.grid[r][c] = 1
                score = self.minmax(self.board.grid, depth - 1, -self.player_id)
                self.board.grid[r][c] = 0  #
                print(f"Checking move ({r},{c}) with score {score}")
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
            print(f"AI plays at {best_move} with score {best_score}")
            if best_move:
                [r, c] = best_move

        self.board.grid[r][c] = 1
        self.drawPieces(c, r)
        self.board.moves_count += 1

        if self.board.verify_check(self.board.grid, 1):
            self.board.gameFinished = True
            self.board.winner = "AI"
            # print("AI wins")
        else:
            self.board.player = "Human"
            self.board.player_id = -1
