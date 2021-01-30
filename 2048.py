import pygame
import sys
import random
import math

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

    def addtile(self):
        emptyslots = []       
        for y in range(4):
            for x in range(4):
                if self.gamedata[y][x] == 0:
                    emptyslots.append([x, y])
        
        addx, addy = emptyslots[random.randint(0, len(emptyslots)-1)]
        if random.randint(0, 9) == 9:
            self.gamedata[addy][addx] = 4
        else:
            self.gamedata[addy][addx] = 2

    def drawtile(self):
        surface = pygame.Surface((100, 100))
        for y in range(4):
            for x in range(4):
                if self.gamedata[y][x] != 0:
                    expon = math.log(self.gamedata[y][x], 2)
                    if expon <= 10:
                        surface.fill((23*expon, 255-23*expon, 23*expon))
                    else:
                        expon %= 10
                        surface.fill((255-23*expon, 255-23*expon, 23*expon))
                    text = font.render(str(self.gamedata[y][x]), True, textcolor)
                    surface.blit(text, (10, 30))
                    gamearea.blit(surface, (x*100, y*100))

    def move_left(self):
        validmove = False
        for y in range(4):
            to_move = []
            space = 0
            for x in range(4):
                if self.gamedata[y][x] == 0:
                    space += 1
                if self.gamedata[y][x]:
                    if space > 0:
                        validmove = True
                    if len(to_move) > 0 and self.gamedata[y][x] == to_move[len(to_move)-1]:
                        to_move[len(to_move)-1] = [to_move[len(to_move)-1]*2]
                        self.gamedata[y][x] = 0
                        validmove = True
                    else:
                        to_move.append(self.gamedata[y][x])
                        self.gamedata[y][x] = 0
            for x in range(4):
                if len(to_move) > 0:
                    if type(to_move[0]) == list:
                        self.gamedata[y][x] = to_move.pop(0)[0]
                    else:
                        self.gamedata[y][x] = to_move.pop(0)
        if validmove:
            self.addtile()

    def move_right(self):
        validmove = False
        for y in range(4):
            to_move = []
            space = 0
            for x in range(4):
                x = 3-x
                if self.gamedata[y][x] == 0:
                    space += 1
                if self.gamedata[y][x]:
                    if space > 0:
                        validmove = True
                    if len(to_move) > 0 and self.gamedata[y][x] == to_move[len(to_move)-1]:
                        to_move[len(to_move)-1] = [to_move[len(to_move)-1]*2]
                        self.gamedata[y][x] = 0
                        validmove = True
                    else:
                        to_move.append(self.gamedata[y][x])
                        self.gamedata[y][x] = 0
            for x in range(4):
                x = 3-x
                if len(to_move) > 0:
                    if type(to_move[0]) == list:
                        self.gamedata[y][x] = to_move.pop(0)[0]
                    else:
                        self.gamedata[y][x] = to_move.pop(0)
        if validmove:
            self.addtile()

    def move_up(self):
        validmove = False
        for x in range(4):
            to_move = []
            space = 0
            for y in range(4):
                if self.gamedata[y][x] == 0:
                    space += 1
                if self.gamedata[y][x]:
                    if space > 0:
                        validmove = True
                    if len(to_move) > 0 and self.gamedata[y][x] == to_move[len(to_move)-1]:
                        to_move[len(to_move)-1] = [to_move[len(to_move)-1]*2]
                        self.gamedata[y][x] = 0
                        validmove = True
                    else:
                        to_move.append(self.gamedata[y][x])
                        self.gamedata[y][x] = 0
            for y in range(4):
                if len(to_move) > 0:
                    if type(to_move[0]) == list:
                        self.gamedata[y][x] = to_move.pop(0)[0]
                    else:
                        self.gamedata[y][x] = to_move.pop(0)
        if validmove:
            self.addtile()

    def move_down(self):
        validmove = False
        for x in range(4):
            to_move = []
            space = 0
            for y in range(4):
                y = 3-y
                if self.gamedata[y][x] == 0:
                    space += 1
                if self.gamedata[y][x]:
                    if space > 0:
                        validmove = True
                    if len(to_move) > 0 and self.gamedata[y][x] == to_move[len(to_move)-1]:
                        to_move[len(to_move)-1] = [to_move[len(to_move)-1]*2]
                        self.gamedata[y][x] = 0
                        validmove = True
                    else:
                        to_move.append(self.gamedata[y][x])
                        self.gamedata[y][x] = 0
            for y in range(4):
                y = 3-y
                if len(to_move) > 0:
                    if type(to_move[0]) == list:
                        self.gamedata[y][x] = to_move.pop(0)[0]
                    else:
                        self.gamedata[y][x] = to_move.pop(0)
        if validmove:
            self.addtile()


gameplay = Game()

gameplay.addtile()
gameplay.addtile()
while True:
    screen.fill(bgcolor)
    screen.blit(gamearea, (0, 100))
    gamearea.fill(gacolor)
    gameplay.drawtile()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gameplay.move_left()
            if event.key == pygame.K_RIGHT:
                gameplay.move_right()
            if event.key == pygame.K_UP:
                gameplay.move_up()
            if event.key == pygame.K_DOWN:
                gameplay.move_down()
    pygame.display.update()
    clock.tick(30)