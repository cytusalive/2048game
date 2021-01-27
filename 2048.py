import pygame
import sys
import random

pygame.init()
pygame.display.set_caption("2048")
screen = pygame.display.set_mode((400, 500))
bgcolor = (230, 180, 100)
screen.fill(bgcolor)
clock = pygame.time.Clock()
gamearea = pygame.Surface((400, 400))
gacolor = (230, 230, 240)
gamearea.fill(gacolor)

gamedata = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

def drawtiles():
    for y in range(len(gamedata)):
        for x in range(len(gamedata[y])):
            tile = pygame.Rect(x*100, y*100, 100, 100)


while True:
    screen.fill(bgcolor)
    screen.blit(gamearea, (0, 100))
    drawtiles()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(30)