import pygame
from minesweeper import Minesweeper
size = width, height = 800,800

bgcolor = 0,0,0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Minesweeper')
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('arial',30)

game = Minesweeper((100,100), 50, 3,font)

running = True

while running:
    screen.fill(bgcolor)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked_cell = game.get_cell_by_pos(event.pos) 
                if clicked_cell != None:
                    game.reveal(clicked_cell)

            elif event.button == 3:
                clicked_cell = game.get_cell_by_pos(event.pos) 
                if clicked_cell != None:
                    game.flag(clicked_cell)
                pass

    if game.check_gameover():
        print("game over")

    game.show(screen)
    pygame.display.update()
    clock.tick(60)