import math

from globals import *


class Board:
    def __init__(self, screen, width, height, rows, cols):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.turn = "X"
        self.gameFinished = False
        self.winner = ""
        self.state = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        self.drawBoard(screen)

    def drawBoard(self, screen):
        # Vertical lines
        pygame.draw.line(screen, "white", pygame.Vector2((self.width / 3), 0),
                         pygame.Vector2((self.width / 3), self.height), width=1)
        pygame.draw.line(screen, "white", pygame.Vector2((2 * self.width / 3), 0),
                         pygame.Vector2((2 * self.width / 3), self.height), width=1)
        pygame.draw.line(screen, "white", pygame.Vector2(self.width, 0),
                         pygame.Vector2(self.width, self.height), width=1)

        # Horizontal lines
        pygame.draw.line(screen, "white", pygame.Vector2(0, (self.height / 3)),
                         pygame.Vector2(self.width, (self.height / 3)), width=1)
        pygame.draw.line(screen, "white", pygame.Vector2(0, (2 * self.height / 3)),
                         pygame.Vector2(self.width, (2 * self.height / 3)), width=1)

    def verify_check(self):
        for i in range(3):

            # Column check
            if self.state[0][i] == self.state[1][i] == self.state[2][i] != 0:
                return True

            # Line check
            if self.state[i][0] == self.state[i][1] == self.state[i][2] != 0:
                return True

        # Diagonals check
        if self.state[0][0] == self.state[1][1] == self.state[2][2] != 0:
            return True
        if self.state[0][2] == self.state[1][1] == self.state[2][0] != 0:
            return True

        """if 0 not in self.state[i]:
            self.gameFinished = True
            print("Draw")"""

        return False

    def drawPieces(self, screen, x, y):
        # Operation to find the row and column
        col = math.floor((self.cols * x) / self.width)
        row = math.floor((self.rows * y) / self.height)

        # Verify if the cursor click is into je board
        if x < self.width and y < self.height:
            if self.turn == "X":
                if self.state[row][col] == 0:
                    self.state[row][col] = -1
                    screen.blit(x_img, (col * (self.width / 3), row * (self.height / 3)))
                    if self.verify_check():
                        self.gameFinished = True
                        self.winner = str(self.turn)
                        print(f"{self.turn} win")
                    else:
                        self.turn = "O"

            elif self.turn == "O":
                if self.state[row][col] == 0:
                    self.state[row][col] = 1
                    screen.blit(o_img, (col * (self.width / 3), row * (self.height / 3)))
                    if self.verify_check():
                        self.gameFinished = True
                        self.winner = str(self.turn)
                        print(f"{self.turn} win")
                    else:
                        self.turn = "X"
