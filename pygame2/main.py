import pygame
import random
from pygame.locals import *
pygame.init()

#Screen
width = 600 #X
height= 600 #Y
SCREEN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")
#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
BROWN = (168, 123, 54)	
#Settings
FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Screen fill
    SCREEN.fill((BROWN))

    #PlayGround

    #Vertical lines
    for i in range(1,3):
        pygame.draw.line(SCREEN, BLACK, (width/3*i,0),(width/3*i,height),5)
    
    #Horizontal lines
    for i in range(1,3):
        pygame.draw.line(SCREEN, BLACK, (0,height/3*i),(width,height/3*i),5)

    #Update screen
    pygame.display.update()

    #Slow cycle
    clock.tick(FPS)

pygame.quit()