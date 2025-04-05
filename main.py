import random

from globals import *
from src.board import Board

pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("TicTacToe-ML")
clock = pygame.time.Clock()
running = True

score_board_surface = screen.subsurface(
    pygame.Rect(BOARD_WIDTH, 0, (WIN_WIDTH - BOARD_WIDTH), WIN_HEIGHT))

# Choose random starting player
starting_player = random.choice([["Human", -1], ["AI", 1]])
board = Board(screen, starting_player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not board.gameFinished:
                if board.player == "Human":
                    board.human_play(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    print(board.grid)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if board.gameFinished:
                    board.rePlay()

    # If there is a draw replay automatically
    if board.moves_count == 9:
        board.gameFinished = True

    score_board_surface.fill((5, 5, 5))
    welcome_txt = font.render("Welcome on TicTacToe-ML", True, "white")
    turn_txt = font.render(f"It's the turn of : {board.player}", True, "blue")

    screen.blit(welcome_txt, ((WIN_WIDTH * 0.65), 100))
    screen.blit(turn_txt, ((WIN_WIDTH * 0.65), 200))

    if board.gameFinished:
        if board.winner == "":
            won_txt = font.render(f"Nobody wins", True, "white")
            won_txt2 = font.render(f"Press SPACE to restart!", True, "white")
            screen.blit(won_txt, ((WIN_WIDTH * 0.7), 600))
            screen.blit(won_txt2, ((WIN_WIDTH * 0.7), 650))
        else:
            won_txt = font.render(f"{board.winner} win !", True, "white")
            won_txt2 = font.render(f"Press SPACE to restart!", True, "white")
            screen.blit(won_txt, ((WIN_WIDTH * 0.7), 600))
            screen.blit(won_txt2, ((WIN_WIDTH * 0.7), 650))

    if not board.gameFinished:
        if board.player == 'AI' and board.player_id == 1:
            board.ai_play()
            print(board.grid)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
