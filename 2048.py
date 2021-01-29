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
                    if self.gamedata[y][x] <= 2048:
                        surface.fill((255, self.gamedata[y][x]/2048 * 255, 255))
                    elif self.gamedata[y][x] <= 4096:
                        surface.fill((255, 255, self.gamedata/4096 * 255))  
                    text = font.render(str(self.gamedata[y][x]), True, textcolor)
                    surface.blit(text, (10, 30))
                    gamearea.blit(surface, (x*100, y*100))

    def move_left(self):
        validmove = False
        for y in range(4):
            space = 0
            for x in range(4):
                if self.gamedata[y][x] == 0:
                    space += 1
                else:
                    if space > 0:
                        self.gamedata[y][x-space] = self.gamedata[y][x]
                        self.gamedata[y][x] = 0
                        validmove = True
                    if x > 0 and self.gamedata[y][x-1] == self.gamedata[y][x]:
                        self.gamedata[y][x-1] *= 2
                        self.gamedata[y][x] = 0
                        validmove = True
        if validmove == True:
            self.addtile()
             
    def move_right(self):
        validmove = False
        for y in range(4):
            space = 0
            for x in range(4):
                x = 3-x
                if self.gamedata[y][x] == 0:
                    space += 1
                else:
                    if space > 0:
                        self.gamedata[y][x+space] = self.gamedata[y][x]
                        self.gamedata[y][x] = 0
                        validmove = True
                    if x < 3 and self.gamedata[y][x+1] == self.gamedata[y][x]:
                        self.gamedata[y][x+1] *= 2
                        self.gamedata[y][x] = 0                        
                        validmove = True
        if validmove == True:
            self.addtile()

    def move_up(self):
        validmove = False
        for x in range(4):
            space = 0
            for y in range(4):
                if self.gamedata[y][x] == 0:
                    space += 1
                else:
                    if space > 0:
                        self.gamedata[y-space][x] = self.gamedata[y][x]
                        self.gamedata[y][x] = 0
                        validmove = True
                    if y > 0 and self.gamedata[y-1][x] == self.gamedata[y][x]:
                        self.gamedata[y-1][x] *= 2
                        self.gamedata[y][x] = 0
                        validmove = True
        if validmove == True:
            self.addtile()

    def move_down(self):
        validmove = False
        for x in range(4):
            space = 0
            for y in range(4):
                y = 3-y
                if self.gamedata[y][x] == 0:
                    space += 1
                else:
                    if space > 0:
                        self.gamedata[y+space][x] = self.gamedata[y][x]
                        self.gamedata[y][x] = 0
                        validmove = True
                    if y < 3 and self.gamedata[y+1][x] == self.gamedata[y][x]:
                        self.gamedata[y+1][x] *= 2
                        self.gamedata[y][x] = 0
                        validmove = True
        if validmove == True:
            self.addtile()                   


gameplay = Game()


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