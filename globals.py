import pygame

pygame.font.init()

WIDTH = 720
HEIGHT = 720

ROWS = 3
COLS = 3

x_img = pygame.transform.scale(pygame.image.load('assets/x.png'), ((WIDTH / ROWS), (HEIGHT / COLS)))
o_img = pygame.transform.scale(pygame.image.load('assets/o.png'), ((WIDTH / ROWS), (HEIGHT / COLS)))

font = pygame.font.Font(None, 48)
