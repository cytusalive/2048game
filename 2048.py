import pygame
import sys
import random

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 32, True)
textcolor = (0, 0, 0)
pygame.display.set_caption("2048")
screen = pygame.display.set_mode((400, 500))
bgcolor = (230, 180, 100)
screen.fill(bgcolor)
clock = pygame.time.Clock()
gamearea = pygame.Surface((400, 400))
gacolor = (230, 230, 240)
gamearea.fill(gacolor)

class Game:
    def __init__(self):
        self.gamedata = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]

    def addtile(self, x, y, value=2):       
        self.gamedata[y][x] = value

    def drawtile(self):
        surface = pygame.Surface((100, 100))
        for y in range(4):
            for x in range(4):
                if self.gamedata[y][x] != 0:
                    surface.fill((255, 255-self.gamedata[y][x], 255))    
                    text = font.render(str(self.gamedata[y][x]), True, textcolor)
                    surface.blit(text, (10, 30))
                    gamearea.blit(surface, (x*100, y*100))

    def move_up(self):
        for x in range(4):
            for y in range(4):
                if   


gameplay = Game()
gameplay.addtile(0, 0, 250)
gameplay.addtile(3, 1, 120)
gameplay.addtile(2, 0, 64)
gameplay.addtile(1, 3, 12)
gameplay.addtile(0, 1, 8)

'''
class Tile:
    def __init__(self, value, xpos, ypos):
        self.value = value
        self.xpos = xpos
        self.ypos = ypos
        self.color = (255-value, 255-value, 255)
        gamedata[ypos][xpos] == 1
    def drawtile(self, field):
        surface = pygame.Surface((100, 100))
        surface.fill(self.color)
        text = font.render(str(self.value), True, textcolor)
        surface.blit(text, (10, 30))
        field.blit(surface, (self.xpos*100, self.ypos*100))
    def move_left(self):
        stack = 0
        for x in range(0, self.xpos):
            if gamedata[self.ypos][x] == 1:
                stack += 1
        if stack < self.xpos:
            gamedata[self.ypos][self.xpos] = 0
            self.xpos = stack
            gamedata[self.ypos][self.xpos] = 1
'''    
    


'''
def drawtiles():
    for y in range(len(gamedata)):
        for x in range(len(gamedata[y])):
            if gamedata[y][x] != 0:
                tile = pygame.Rect(x*100, y*100, 100, 100)
                pygame.draw.rect(gamearea, (200, 50, 50), tile, 0, 10)
'''


while True:
    screen.fill(bgcolor)
    screen.blit(gamearea, (0, 100))
    gamearea.fill(gacolor)
    gameplay.drawtile()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(30)