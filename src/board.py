import math

from globals import *


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.player = "Human"
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

    def verify_check(self):
        for i in range(3):

            # Column check
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != 0:
                return True

            # Line check
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != 0:
                return True
        # Diagonals check
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != 0:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != 0:
            return True

        if self.moves_count == 10:
            self.gameFinished = True
            self.winner = "Nobody"
            print('tie')

        return False

    def empty_cells(self):
        cells = []
        for r in range(3):
            for c in range(3):
                if self.grid[r][c] == 0:
                    cells.append([r, c])

        return cells

    def human_play(self, x, y):
        if self.player == "Human":
            # Operation to find the row and column
            col = math.floor((COLS * x) / BOARD_WIDTH)
            row = math.floor((ROWS * y) / BOARD_HEIGHT)

            # Verify if the cursor click is into  the board
            if x < BOARD_WIDTH and y < BOARD_HEIGHT:
                if [row, col] in self.empty_cells():
                    self.grid[row][col] = -1
                    self.drawPieces(col, row)

                    if self.verify_check():
                        self.gameFinished = True
                        self.winner = str(self.player)
                        print(f"{self.player} win")
                    else:
                        self.player = "AI"

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
