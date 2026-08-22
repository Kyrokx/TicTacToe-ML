import random
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

    @staticmethod
    def verify_check(grid, player_id):
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