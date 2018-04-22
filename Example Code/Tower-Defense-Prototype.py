# code based of of the code from the pygame tutorial at pythonprogramming.net.

import pygame
import random
import math

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tower Defense Prototype")


crashed = False

bob = pygame.image.load('Bob.png')
coin = pygame.image.load('Dot.png')
class Dot(object):
    def __init__(self,points):
        self.points = points
        self.point = 0
        self.pos = self.points[self.point]
        self.img = coin

    def display(self):
        if self.point == len(points)-1:
            return True
        else:
            yD = self.points[self.point + 1][1] - self.points[self.point][1]
            xD = self.points[self.point + 1][0] - self.points[self.point][0]
            if xD == 0:
                x = 0
                if yD < 0: y = -1
                elif yD > 0: y = 1
                else: y = 0
            else:
                y = yD * (1/math.sqrt(yD ** 2 + xD ** 2))
                x = xD * (1/math.sqrt(yD ** 2 + xD ** 2))
            self.pos[0] += x
            self.pos[1] += y
        gameDisplay.blit(self.img, [int(round(self.pos[0])),int(round(self.pos[1]))])
        if round(self.pos[0]) == self.points[self.point + 1][0] and round(self.pos[1]) == self.points[self.point + 1][1]: self.point += 1
        return False
c = 0
done = False
points = [[10,50],[600,50],[600,550],[100,550],[100,150],[400,150],[400,400],[200,400],[200,200],[300,300]]
listy = [Dot(points)]
pointlist = []
for pair in [[10,50],[600,50],[600,550],[100,550],[100,150],[400,150],[400,400],[200,400],[200,200],[300,300]]:
    pointlist.append((pair[0]+15, pair[1]+15))
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            listy.append(Dot([[10,50],[600,50],[600,550],[100,550],[100,150],[400,150],[400,400],[200,400],[200,200],[300,300]]))
    gameDisplay.fill((0,0,0))
    pygame.draw.lines(gameDisplay,(255,153,51),False,pointlist,10)
    for dot in listy:
        if dot is not None:
            if dot.display(): listy.pop(0)
    pygame.display.update()

    
    

pygame.quit()
quit()
