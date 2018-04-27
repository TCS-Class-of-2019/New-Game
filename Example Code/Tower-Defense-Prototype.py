# code based of of the code from the pygame tutorial at pythonprogramming.net.

import pygame # these import the needed modules
import random
import math

pygame.init() # this initializes the pygame module

gameDisplay = pygame.display.set_mode((800,600)) # makes a window
pygame.display.set_caption("TOWER DEFENSE") # sets the caption
gameIcon = pygame.image.load('Icon.png') # loads the icon image
pygame.display.set_icon(gameIcon) # sets the icon

coin = pygame.image.load('Dot.png') #loads the dot image

class Dot(object):
    def __init__(self,points,speed=1): #creates an instance of the Dot object
        self.points = points # gives it the set of points in the map
        self.point = 0 #it starts on point 0
        self.pos = list(self.points[self.point])
        self.img = coin # this is its apperance
        self.speed = speed # this is how fast it'll go
        #if self.speed > 1: self.speed = 1 ----> I wanted a speed limit, but that was before I tested for lag
        #elif self.speed < .1: self.speed = .1
        

    def display(self): # this method displays th dot on the screen: it also handles movement
        if self.point == len(self.points)-1: # if it reached the end, kill it (done in the loop)
            return True
        else:
            yD = self.points[self.point + 1][1] - self.points[self.point][1] # change in y
            xD = self.points[self.point + 1][0] - self.points[self.point][0] # change in x
            if xD == 0: # special case for no slope
                x = 0
                if yD < 0: y = -1 * self.speed
                elif yD > 0: y = 1 * self.speed
                else: y = 0
            else: # otherwise just do some math to figure out the slope and distance traveled
                y = self.speed * yD * (1/math.sqrt(yD ** 2 + xD ** 2)) # distance formula to make it a vector with magnitude == speed
                x = self.speed * xD * (1/math.sqrt(yD ** 2 + xD ** 2))
            self.pos[0] += x # update the dot's position
            self.pos[1] += y
        gameDisplay.blit(self.img, [int(round(self.pos[0])),int(round(self.pos[1]))]) #put it on the screen rounded to the nearest pixel
        xNow = round(self.pos[0]) #               I caught this during testing
        xGoal = self.points[self.point + 1][0] #  Sometimes, when the dot is moving quickly it misses the target point
        yNow = round(self.pos[1]) #               So, I made a "net" of sorts to keep the dot from missing the next point
        yGoal = self.points[self.point + 1][1] #  This long if statement makes sure that the position isn't past what it should be
        if (xNow ==  xGoal and  yNow == yGoal) or (self.pos[0] > self.points[self.point +1][0] and x > 0) or (self.pos[0] < self.points[self.point +1][0] and x < 0) or (self.pos[1] < self.points[self.point +1][1] and y < 0) or (self.pos[1] > self.points[self.point +1][1] and y > 0):
            self.point += 1 # if it missed it, put it back to where it should be
            self.pos = list(self.points[self.point]) # and make its position the point, for simplicity's sake
        return False

def intro(): # this creates the intro loop 
    done = False
    while not done: # keep goin' till we're done
        gameDisplay.fill((0,0,0)) # fill it in rbg black
        mouse = pygame.mouse.get_pos() # get cursor position
        if 330 < mouse[0] < 470 and 250 < mouse[1] < 350:  # if it's in our box...
            pygame.draw.rect(gameDisplay,(0,255,0), (330,250,140,100)) # ...make it green...
        else:
            pygame.draw.rect(gameDisplay,(255,0,0), (330,250,140,100)) # ...else red.
        font = pygame.font.Font('freesansbold.ttf',50)
        TextSurf = font.render("Start",True,(127,127,127)) # start text
        TextRect = TextSurf.get_rect() 
        TextRect.center = ((400),(300))
        gameDisplay.blit(TextSurf, TextRect)
        font = pygame.font.Font('freesansbold.ttf',80)
        TextSurf = font.render("TOWER DEFENSE",True,(127,127,127)) # title text
        TextRect = TextSurf.get_rect()
        TextRect.center = ((400),(150))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update() # this command actually makes things appear, otherwise they'd just be queued.
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if they quit...
                pygame.quit() # ...quit.
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # if they hit the start button, our job is done.
                if 330 < event.pos[0] < 470 and 250 < event.pos[1] < 350: done = True

def displayScore(text): # this method displays, you guessed it, the score.
    font = pygame.font.Font('freesansbold.ttf',20)
    TextSurf = font.render(text,True,(127,127,127))
    TextRect = TextSurf.get_rect()
    TextRect.center = ((740),(25))
    gameDisplay.blit(TextSurf, TextRect)

def displayLoss(): # this method displays the loss screen for a second or two.
    c = 0
    gameDisplay.fill((0,0,0))
    while c < 1000:
        font = pygame.font.Font('freesansbold.ttf',80)
        TextSurf = font.render("YOU LOSE",True,(127,127,127))
        TextRect = TextSurf.get_rect()
        TextRect.center = ((400),(300))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        c += 1 # I wish python had an increment operator in times like these.

def gameLoop():
    c = 0
    lives = 1
    done = False # not done yet                   This below is the long list of points in our crazy map.
    points =((10,50),(600,50),(600,550),(100,550),(100,150),(400,150),(400,400),(200,400),(200,200),(300,300),(500,300),(300,100),(700,100),(700,570),(50,570),(320,345))
    parameter = list(points)# create a duplicate to preserve the original, I don't know why I called it parameter...
    listy = [] # ... in the actual game we'll make things cleaner
    pointlist = []
    for pair in points:
        pointlist.append((pair[0]+15, pair[1]+15)) # So the dots actually follow the path (image overlay causes it to be off-center)
    while done == False: # or 'not done', either way looking back at it.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                parameter = list(points)
                if event.key == pygame.K_1: listy.append(Dot(parameter,.1)) # if you press a number 1,2,3...
                elif event.key == pygame.K_2: listy.append(Dot(parameter,.2))
                elif event.key == pygame.K_3: listy.append(Dot(parameter,.3))
                elif event.key == pygame.K_4: listy.append(Dot(parameter,.4))
                elif event.key == pygame.K_5: listy.append(Dot(parameter,.5)) # each of these creates a dot with speed increasing...
                elif event.key == pygame.K_6: listy.append(Dot(parameter,.6))
                elif event.key == pygame.K_7: listy.append(Dot(parameter,.7))
                elif event.key == pygame.K_8: listy.append(Dot(parameter,.8))
                elif event.key == pygame.K_9: listy.append(Dot(parameter,.9))
                else: listy.append(Dot(parameter,3)) # ...until here, where it's pretty fast.
        gameDisplay.fill((0,0,0))
        pygame.draw.lines(gameDisplay,(255,153,51),False,pointlist,10) #draw our map using this handy function
        for dot in listy:
            if dot is not None: # I love that I have to include this (sarcasm)
                if dot.display():
                    listy.remove(dot) # if the dot made it to the end, then kill it and kill one of your lives.
                    lives -= 1
        displayScore(str(lives) + " lives") # display the score
        pygame.display.update()
        if lives == 0: return # uh-oh, you ran out of lives, so show the loss screen

### MAIN ###
        
intro() # calls the intro then gameloop then loss screen
gameLoop()
displayLoss()
    

pygame.quit() # quit the game module and python code
quit()

# DISCLAIMER: I haven't tested it with the new comments so if it doesn't work know that it used to.
# Also, I apologize for any tpyos. :P
