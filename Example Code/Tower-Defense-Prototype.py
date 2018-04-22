# code based of of the code from the pygame tutorial at pythonprogramming.net.

import pygame
import random
import math

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("TOWER DEFENSE")
gameIcon = pygame.image.load('Icon.png')
pygame.display.set_icon(gameIcon)


crashed = False

coin = pygame.image.load('Dot.png')
class Dot(object):
    def __init__(self,points,speed=1):
        self.points = points
        self.point = 0
        self.pos = list(self.points[self.point])
        self.img = coin
        self.speed = speed
        #if self.speed > 1: self.speed = 1
        #elif self.speed < .1: self.speed = .1
        

    def display(self):
        if self.point == len(self.points)-1:
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
        xNow = round(self.pos[0])
        xGoal = self.points[self.point + 1][0]
        yNow = round(self.pos[1])
        yGoal = self.points[self.point + 1][1]
        if (xNow ==  xGoal and  yNow == yGoal) or (self.pos[0] > self.points[self.point +1][0] and x > 0) or (self.pos[0] < self.points[self.point +1][0] and x < 0) or (self.pos[1] < self.points[self.point +1][1] and y < 0) or (self.pos[1] > self.points[self.point +1][1] and y > 0):
            self.point += 1
            self.pos = list(self.points[self.point])
        return False

def intro():
    done = False
    while not done:
        gameDisplay.fill((0,0,0))
        mouse = pygame.mouse.get_pos()
        if 330 < mouse[0] < 470 and 250 < mouse[1] < 350:  
            pygame.draw.rect(gameDisplay,(0,255,0), (330,250,140,100))
        else:
            pygame.draw.rect(gameDisplay,(255,0,0), (330,250,140,100))
        font = pygame.font.Font('freesansbold.ttf',50)
        TextSurf = font.render("Start",True,(127,127,127))
        TextRect = TextSurf.get_rect() 
        TextRect.center = ((400),(300))
        gameDisplay.blit(TextSurf, TextRect)
        font = pygame.font.Font('freesansbold.ttf',80)
        TextSurf = font.render("TOWER DEFENSE",True,(127,127,127))
        TextRect = TextSurf.get_rect()
        TextRect.center = ((400),(150))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 330 < event.pos[0] < 470 and 250 < event.pos[1] < 350: done = True

def displayScore(text):
    font = pygame.font.Font('freesansbold.ttf',20)
    TextSurf = font.render(text,True,(127,127,127))
    TextRect = TextSurf.get_rect()
    TextRect.center = ((740),(25))
    gameDisplay.blit(TextSurf, TextRect)

def displayLoss():
    c = 0
    gameDisplay.fill((0,0,0))
    while c < 1000:
        font = pygame.font.Font('freesansbold.ttf',80)
        TextSurf = font.render("YOU LOSE",True,(127,127,127))
        TextRect = TextSurf.get_rect()
        TextRect.center = ((400),(300))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        c += 1

def gameLoop():
    c = 0
    lives = 1
    done = False
    points =((10,50),(600,50),(600,550),(100,550),(100,150),(400,150),(400,400),(200,400),(200,200),(300,300),(500,300),(300,100),(700,100),(700,570),(50,570),(320,345))
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
                else: listy.append(Dot(parameter,3))
        gameDisplay.fill((0,0,0))
        pygame.draw.lines(gameDisplay,(255,153,51),False,pointlist,10)
        for dot in listy:
            if dot is not None:
                if dot.display():
                    listy.remove(dot)
                    lives -= 1
        displayScore(str(lives) + " lives")
        pygame.display.update()
        if lives == 0: return

intro()
gameLoop()
displayLoss()
    

pygame.quit()
quit()
