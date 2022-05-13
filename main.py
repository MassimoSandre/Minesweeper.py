import pygame
from minesweeper import Minesweeper
size = width, height = 800,800

bgcolor = 0,0,0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Minesweeper')
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('arial',10)

game = Minesweeper((0,0),font)

running = True

while running:
    screen.fill(bgcolor)

    for event in pygame.event.get():
        pass

    
    pygame.display.update()
    clock.tick(60)