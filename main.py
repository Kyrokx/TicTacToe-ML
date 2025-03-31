import pygame
from globals import *
from src.Board import Board

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("TicTacToe-ML")
clock = pygame.time.Clock()
running = True

board = Board(screen, WIDTH, HEIGHT, ROWS, COLS)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not board.gameFinished:
                board.drawPieces(screen, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            else:
                won_txt = font.render(f"<{board.turn}> WON", True, "white")
                screen.blit(won_txt, (1000, 600)).update(won_txt.get_rect())

    welcome_txt = font.render("Welcome on TicTacToe-ML", False, "white")
    turn_txt = font.render(f"It's <{board.turn}> move", False, "blue")

    screen.blit(welcome_txt, (800, 200)).update(welcome_txt.get_rect())
    screen.blit(turn_txt, (1000, 400)).update(turn_txt.get_rect())

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
