import math
from math import *
import random

import numpy as np
from globals import *


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.player = "Human"
        self.player_id = -1
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

    def check_game(self, board, player):
        for row in board:
            if row[0] == row[1] == row[2] == player:
                print(player, "gagne")
                return True

        for col in range(len(board)):
            check = []
            for row in board:
                check.append(row[col])
            if check.count(player) == len(check) and check[0] != 0:
                print("player", player, "gagne")
                return True

        diags = []
        for indx in range(len(board)):
            diags.append(board[indx][indx])
        if diags.count(player) == len(diags) and diags[0] != 0:
            print(player, "gagne")
            return True

        diags_2 = []
        for indx, rev_indx in enumerate(reversed(range(len(board)))):
            diags_2.append(board[indx][rev_indx])
        if diags_2.count(player) == len(diags_2) and diags_2[0] != 0:
            print(player, "gagne")
            return True

    def verify_check(self, player):
        for i in range(3):
            # Column check
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] == player:
                return True

            # Line check
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] == player:
                return True
        # Diagonals check
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == player:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == player:
            return True

        """if self.moves_count == 10:
            self.gameFinished = True
            self.winner = 'Nobody'
            print('tie')

        return False """

    def empty_cells(self):
        cells = []
        for r in range(3):
            for c in range(3):
                if self.grid[r][c] == 0:
                    cells.append([r, c])

        print(cells)
        return cells

    def human_play(self, x, y):  # -1
        if self.player == "Human":
            # Operation to find the row and column
            col = math.floor((COLS * x) / BOARD_WIDTH)
            row = math.floor((ROWS * y) / BOARD_HEIGHT)

            # Verify if the cursor click is into  the board
            if x < BOARD_WIDTH and y < BOARD_HEIGHT:
                if [row, col] in self.empty_cells():
                    self.grid[row][col] = -1
                    self.drawPieces(col, row)

                    if self.check_game(self.grid, -1):
                        self.gameFinished = True
                        self.winner = str(self.player)
                        print(f"{self.player} win")
                    else:
                        self.player = "AI"
                        self.player_id = 1

                self.moves_count += 1

    def ai_play(self):
        depth = 3
        if depth == 0 or self.is_terminal_node():
            return

        if self.player == "AI" and self.player_id == 1:
            """best_move = self.minmax(depth, 0, 0, self.player_id)
            # print(best_move)
            r, c = best_move[0], best_move[1]

            self.drawPieces(c, r)"""

            best_move = self.get_best_move()
            if best_move is None:
                best_move = random.choice(self.empty_cells())
                print(f'+++++++++{best_move}+++++++++++++')

            print(f'*************{best_move}***************')
            r, c = best_move[0], best_move[1]
            self.drawPieces(c, r)
            self.grid[r][c] = 1
            if self.check_game(self.grid, 1):
                self.gameFinished = True
                self.winner = str(self.player)
                print(f"{self.player} win")
            else:
                self.player = "Human"
                self.player_id = -1

        self.moves_count += 1

    def drawPieces(self, col, row):
        if self.player == "Human":
            self.screen.blit(x_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))

        elif self.player == "AI":
            self.screen.blit(o_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))

    def rePlay(self):
        self.screen.fill((0, 0, 0))
        self.player = "Human"
        self.moves_count = 0
        self.gameFinished = False
        self.winner = ""
        self.grid = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        self.drawBoard()
        pygame.display.update()
        pygame.display.flip()

    def is_terminal_node(self):
        return self.check_game(self.grid, (-1)) or self.check_game(self.grid, 1)

    def evaluate(self):
        if self.check_game(self.grid, (-1)):
            score = -100
        elif self.check_game(self.grid, 1):
            score = 100
        else:
            score = 0

        return score

    def minmax(self, depth, isMax):
        """if player_number == 1:
            best = [1, 1, -np.inf]
        else:
            best = [1, 1, +np.inf]"""

        self.evaluate()

        if isMax:
            best_score = -np.inf

            for [r, c] in self.empty_cells():
                self.grid[r][c] = 1
                score = self.minmax(depth + 1, False)
                self.grid[r][c] = 0
                # Update the best score
                best_score = max(score, best_score)
            return best_score

        else:
            # if it is the minimizing player's turn (human), we want to minimize the score
            best_score = np.inf
            for [r, c] in self.empty_cells():
                # Make a calculating move
                self.grid[r][c] = -1
                # Recursively call minimax with the next depth and the maximizing player
                score = self.minmax(depth + 1, True)
                # Reset the move
                self.grid[r][c] = 0
                # Update the best score
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        """Find the best move for AI using minimax"""
        best_score = -np.inf
        best_move = None  # [1, 1]

        for [r, c] in self.empty_cells():
            # Make a calculating move
            self.grid[r][c] = 1
            # Recursively call minimax with the next depth and the minimizing player
            score = self.minmax(1, True)
            # Reset the move
            self.grid[r][c] = 0

            # Update the best score
            if score > best_score:
                best_score = score
                best_move = [r, c]

        return best_move
