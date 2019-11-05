# Name: Moustafa Eid
# Date: April 13 2017
# Class: ICS3U1-03
# Description: Graphics Test Question 2

import pygame
import math
import random

#setting up pygame and screen
pygame.init() 
SIZE = (500,500) 
screen = pygame.display.set_mode(SIZE)

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,51)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
xsize = SIZE[0]
ysize = SIZE[1]
midx = xsize // 2
midy = ysize // 2
radius = xsize // 4

pygame.draw.rect (screen,RED,pygame.Rect(0,0,xsize,ysize))
pygame.draw.circle(screen,GREEN, (xsize//4,ysize//4),radius)
pygame.draw.circle(screen,BLUE, (xsize - (xsize//4),ysize//4),radius)
pygame.draw.circle(screen,GREEN, (xsize - (xsize//4),ysize - (ysize//4)),radius)
pygame.draw.circle(screen,BLUE, (xsize//4,ysize - (ysize//4)),radius)
pygame.draw.rect (screen,BLACK,pygame.Rect(xsize//4,ysize//4,xsize//2,ysize//2),5)
pygame.draw.line(screen,WHITE,(xsize//2,ysize//2),(xsize,ysize),20)
pygame.draw.line(screen,WHITE,(xsize//2,ysize//2),(0,ysize),20)







pygame.display.flip()
