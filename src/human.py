import math
import random

import numpy as np

from globals import *
from .board import Board



class Human:
    def __init__(self, board:Board):
        self.board = board
        self.screen = board.screen
        self.player = "Human"
        self.player_id = -1
        
    def drawPieces(self, col, row):
        
        self.screen.blit(x_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))
        
        # if self.player == "Human":
        #     self.screen.blit(x_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))

        # elif self.player == "AI":
        #     self.screen.blit(o_img, (col * (BOARD_WIDTH / 3), row * (BOARD_HEIGHT / 3)))
        


    def play(self, x, y):
        # Operation to find the row and column
        col = math.floor((COLS * x) / BOARD_WIDTH)
        row = math.floor((ROWS * y) / BOARD_HEIGHT)

        # Verify if the cursor click is into the board
        if x < BOARD_WIDTH and y < BOARD_HEIGHT:
            if [row, col] in self.board.empty_cells():
                self.board.grid[row][col] = -1
                self.drawPieces(col, row)
                print(self.board.is_terminal_node(self.board.grid))
                if self.board.verify_check(self.board.grid, -1):
                    self.board.gameFinished = True
                    self.board.winner = str(self.player)
                    print(f"{self.player} win")
                else:
                    self.board.player = "AI"
                    self.board.player_id = 1

            self.board.moves_count += 1