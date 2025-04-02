import math
from math import *
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

    def check_game(self,board, player):
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

                    if self.verify_check(-1):
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
            best_move = self.minmax(depth, 0, 0, self.player_id)
            print(best_move)
            r, c = best_move[0], best_move[1]

            self.drawPieces(c, r)

            if self.verify_check(1):
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
        return self.check_game(self.grid,-1) or self.check_game(self.grid,(1))

    def evaluate(self):
        if self.check_game(self.grid,-1):
            score = -5
        elif self.check_game(self.grid,1):
            score = 5
        else:
            score = 0

        return score

    def minmax(self, depth, alpha, beta, player_number):
        """if player_number == 1:
            best = [1, 1, -np.inf]
        else:
            best = [1, 1, +np.inf]"""

        if depth == 0:
            score = self.evaluate()
            return [1, 1, score]

        for location in self.empty_cells():
            r, c = location[0], location[1]

            self.grid[r][c] = player_number
            info = self.minmax(depth - 1, alpha, beta, -player_number)
            self.grid[r][c] = 0

            return info
