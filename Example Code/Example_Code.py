import pygame
import random

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Coin Collector")

crashed = False

bob = pygame.image.load('Bob.png')
coin = pygame.image.load('Coin.png')

def move(x,y):
    gameDisplay.blit(bob, (x,y))

def makeNewCoin():
    x, y = random.randint(0,780), random.randint(0,580)
    gameDisplay.blit(coin, (x,y))
    return x,y

def displayCoin(x,y):
    gameDisplay.blit(coin, (x, y))

x = 360
y = 480
xMove = 0
yMove = 0
score = 0

cx, cy = makeNewCoin()

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xMove = 2
            elif event.key == pygame.K_LEFT:
                xMove = -2
            elif event.key == pygame.K_UP:
                yMove = -2
            elif event.key == pygame.K_DOWN:
                yMove = 2
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                xMove = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                yMove = 0
            
    x += xMove
    y += yMove
    if x > 770: x = 770
    if x < 0: x = 0
    if y > 540: y = 540
    if y < 0: y = 0
    gameDisplay.fill((1,1,1))

    if cx + 20 > x and cx < x + 30 and cy + 20 > y and cy < y + 60:
        score += 10
        cx, cy = makeNewCoin()
    else: displayCoin(cx,cy)
    
    
    move(x,y)


    pygame.display.update()

pygame.quit()
quit()
