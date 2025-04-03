import math
import random

import numpy as np

from globals import *


class Board:
    def __init__(self, screen, starting_player):
        self.screen = screen
        self.player = starting_player[0]
        self.player_id = starting_player[1]
        self.gameFinished = False
        self.winner = ""
        self.moves_count = 0
        self.grid = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

        self.drawBoard()

    def drawBoard(self):
        # Vertical lines
        pygame.draw.line(self.screen, "white", pygame.Vector2((BOARD_WIDTH / 3), 0),
                         pygame.Vector2((BOARD_WIDTH / 3), BOARD_HEIGHT), width=1)
        pygame.draw.line(self.screen, "white", pygame.Vector2((2 * BOARD_WIDTH / 3), 0),
                         pygame.Vector2((2 * BOARD_WIDTH / 3), BOARD_HEIGHT), width=1)
        pygame.draw.line(self.screen, "white", pygame.Vector2(BOARD_WIDTH, 0),
                         pygame.Vector2(BOARD_WIDTH, BOARD_HEIGHT), width=1)

        # Horizontal lines
        pygame.draw.line(self.screen, "white", pygame.Vector2(0, (BOARD_HEIGHT / 3)),
                         pygame.Vector2(BOARD_WIDTH, (BOARD_HEIGHT / 3)), width=1)
        pygame.draw.line(self.screen, "white", pygame.Vector2(0, (2 * BOARD_HEIGHT / 3)),
                         pygame.Vector2(BOARD_WIDTH, (2 * BOARD_HEIGHT / 3)), width=1)

    def verify_check(self, grid, player_id):
        for i in range(3):
            # Column check
            if grid[0][i] == grid[1][i] == grid[2][i] == player_id:
                return True

            # Line check
            if grid[i][0] == grid[i][1] == grid[i][2] == player_id:
                return True
        # Diagonals check
        if grid[0][0] == grid[1][1] == grid[2][2] == player_id:
            return True
        if grid[0][2] == grid[1][1] == grid[2][0] == player_id:
            return True

        """if self.moves_count == 10:
            self.gameFinished = True
            self.winner = 'Nobody'
            print('tie')

        return False"""

    def empty_cells(self):
        cells = []
        for r in range(3):
            for c in range(3):
                if self.grid[r][c] == 0:
                    cells.append([r, c])
        return cells

    def human_play(self, x, y):
        # Operation to find the row and column
        col = math.floor((COLS * x) / BOARD_WIDTH)
        row = math.floor((ROWS * y) / BOARD_HEIGHT)

        # Verify if the cursor click is into the board
        if x < BOARD_WIDTH and y < BOARD_HEIGHT:
            if [row, col] in self.empty_cells():
                self.grid[row][col] = -1
                self.drawPieces(col, row)
                print(self.is_terminal_node(self.grid))
                if self.verify_check(self.grid, -1):
                    self.gameFinished = True
                    self.winner = str(self.player)
                    print(f"{self.player} win")
                else:
                    self.player = "AI"
                    self.player_id = 1

            self.moves_count += 1

    def drawPieces(self, col, row):
        if self.player == "Human":
            self.screen.blit(x_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))

        elif self.player == "AI":
            self.screen.blit(o_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))

    def rePlay(self):
        self.screen.fill((0, 0, 0))
        starting_player = random.choice([["Human", -1], ["AI", 1]])
        self.player = starting_player[0]
        self.player_id = starting_player[1]
        self.moves_count = 0
        self.gameFinished = False
        self.winner = ""
        self.grid = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        self.drawBoard()

    def is_terminal_node(self, grid):
        if self.verify_check(grid, -1) or self.verify_check(grid, 1):
            return True
        else:
            return False

    def evaluate(self, grid, depth):
        if self.verify_check(grid, 1):
            return 10 - depth
        elif self.verify_check(grid, -1):
            return -10 + depth
        return 0

    def minmax(self, grid, depth, player_id):
        score = self.evaluate(grid, depth)

        if abs(score) == 10 or depth == 0:
            print(f"Returning score {score} at depth {depth}")
            return score

        if player_id == -1:  # It's human turn: We want to minimize
            best_score = np.inf
            for [r, c] in self.empty_cells():
                grid[r][c] = -1
                best_score = min(best_score, self.minmax(grid, depth - 1, -player_id))
                grid[r][c] = 0
            print(f"Best score for human: {best_score}")
            return best_score

        else:  # It's AI turn: We want to maximize
            best_score = -np.inf
            for [r, c] in self.empty_cells():
                grid[r][c] = 1
                best_score = max(best_score, self.minmax(grid, depth - 1, -player_id))
                grid[r][c] = 0
            print(f"Best score for AI: {best_score}")
            return best_score

    def ai_play(self):
        depth = len(self.empty_cells())

        if depth == 0 or self.is_terminal_node(self.grid):
            return

        if depth == 9:
            r, c = random.choice(self.empty_cells())

        else:
            best_score = -np.inf
            best_move = None

            for [r, c] in self.empty_cells():
                self.grid[r][c] = 1
                score = self.minmax(self.grid, depth - 1, -self.player_id)
                self.grid[r][c] = 0  #
                print(f"Checking move ({r},{c}) with score {score}")
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
            print(f"AI plays at {best_move} with score {best_score}")
            if best_move:
                r, c = best_move

        self.grid[r][c] = 1
        self.drawPieces(c, r)
        self.moves_count += 1

        if self.verify_check(self.grid, 1):
            self.gameFinished = True
            self.winner = "AI"
            print("AI wins")
        else:
            self.player = "Human"
            self.player_id = -1
