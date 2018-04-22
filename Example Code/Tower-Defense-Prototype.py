# code based of of the code from the pygame tutorial at pythonprogramming.net.

import pygame
import random
import math

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tower Defense Prototype")


crashed = False

coin = pygame.image.load('Dot.png')
class Dot(object):
    def __init__(self,points,speed=1):
        self.points = points
        self.point = 0
        self.pos = list(self.points[self.point])
        self.img = coin
        self.speed = speed
        if self.speed > 1: self.speed = 1
        elif self.speed < .1: self.speed = .1
        

    def display(self):
        if self.point == len(points)-1:
            return True
        else:
            yD = self.points[self.point + 1][1] - self.points[self.point][1]
            xD = self.points[self.point + 1][0] - self.points[self.point][0]
            if xD == 0:
                x = 0
                if yD < 0: y = -1 * self.speed
                elif yD > 0: y = 1 * self.speed
                else: y = 0
            else:
                y = self.speed * yD * (1/math.sqrt(yD ** 2 + xD ** 2))
                x = self.speed * xD * (1/math.sqrt(yD ** 2 + xD ** 2))
            self.pos[0] += x
            self.pos[1] += y
        gameDisplay.blit(self.img, [int(round(self.pos[0])),int(round(self.pos[1]))])
        if round(self.pos[0]) == self.points[self.point + 1][0] and round(self.pos[1]) == self.points[self.point + 1][1]: self.point += 1
        return False
c = 0
done = False
points =((10,50),(600,50),(600,550),(100,550),(100,150),(400,150),(400,400),(200,400),(200,200),(300,300))
parameter = list(points)
listy = []
pointlist = []
for pair in points:
    pointlist.append((pair[0]+15, pair[1]+15))
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            parameter = list(points)
            if event.key == pygame.K_1: listy.append(Dot(parameter,.1))
            elif event.key == pygame.K_2: listy.append(Dot(parameter,.2))
            elif event.key == pygame.K_3: listy.append(Dot(parameter,.3))
            elif event.key == pygame.K_4: listy.append(Dot(parameter,.4))
            elif event.key == pygame.K_5: listy.append(Dot(parameter,.5))
            elif event.key == pygame.K_6: listy.append(Dot(parameter,.6))
            elif event.key == pygame.K_7: listy.append(Dot(parameter,.7))
            elif event.key == pygame.K_8: listy.append(Dot(parameter,.8))
            elif event.key == pygame.K_9: listy.append(Dot(parameter,.9))
            else: listy.append(Dot(parameter,1))
    gameDisplay.fill((0,0,0))
    pygame.draw.lines(gameDisplay,(255,153,51),False,pointlist,10)
    for dot in listy:
        if dot is not None:
            if dot.display(): listy.remove(dot)
    pygame.display.update()

    
    

pygame.quit()
quit()
