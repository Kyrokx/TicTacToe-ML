import pygame

pygame.font.init()

WIN_WIDTH = 1280
WIN_HEIGHT = 720

BOARD_WIDTH = 720
BOARD_HEIGHT = 720

ROWS = 3
COLS = 3

x_img = pygame.transform.scale(pygame.image.load('assets/x.png'), ((BOARD_WIDTH / ROWS), (BOARD_HEIGHT / COLS)))
o_img = pygame.transform.scale(pygame.image.load('assets/o.png'), ((BOARD_WIDTH / ROWS), (BOARD_HEIGHT / COLS)))

font = pygame.font.Font("assets/font/Quicksand-VariableFont_wght.ttf", 36)
