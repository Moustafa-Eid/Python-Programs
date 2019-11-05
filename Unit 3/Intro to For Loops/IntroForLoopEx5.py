# Name: Moustafa Eid
# Date: April 27th 2017
# Class: ICS3U1-03
# Description: Circle moving from left to right

import pygame
import math

#setting up pygame and screen
pygame.init() 
SIZE = (800, 700) 
screen = pygame.display.set_mode(SIZE)
speed = 30

pygame.display.flip ()

# loop that moves circle from left to right
while (True):
    for count in range(SIZE[0]+1):
        pygame.draw.circle(screen, (0,0,255), (count,350),100)
        pygame.display.flip ()
        pygame.draw.rect (screen,(0,0,0), pygame.Rect (0,0,SIZE[0],SIZE[1]))
    