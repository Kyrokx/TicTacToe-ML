import pygame

from globals import *
from src.board import Board

pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("TicTacToe-ML")
clock = pygame.time.Clock()
running = True

score_board_surface = screen.subsurface(
    pygame.Rect(BOARD_WIDTH, 0, (WIN_WIDTH - BOARD_WIDTH), WIN_HEIGHT))

board = Board(screen, BOARD_WIDTH, BOARD_HEIGHT, ROWS, COLS)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not board.gameFinished:
                board.drawPieces(screen, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if board.gameFinished:
                    board.rePlay(screen)

    score_board_surface.fill((5, 5, 5))
    welcome_txt = font.render("Welcome on TicTacToe-ML", True, "white")
    turn_txt = font.render(f"It's the turn of : {board.turn}", True, "blue")

    screen.blit(welcome_txt, ((WIN_WIDTH*0.65), 100))
    screen.blit(turn_txt, ((WIN_WIDTH*0.65), 200))

    if board.gameFinished:
        won_txt = font.render(f"{board.winner} WIN !", True, "white")
        screen.blit(won_txt, ((WIN_WIDTH*0.7), 600))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
