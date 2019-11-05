# Name: Moustafa Eid
# Date: March 13th 2017
# Class: ICS3U1-03
# Description: Animation of a Tic Tac Toe Game

import pygame
import math

#setting up pygame and screen
pygame.init() 
SIZE = (800, 700) 
screen = pygame.display.set_mode(SIZE)

pygame.draw.rect(screen, (232, 171, 58), pygame.Rect(0,600,800,100))
pygame.draw.rect(screen, (204, 151, 55), pygame.Rect(0,515,800,85))
pygame.draw.rect(screen, (196, 153, 76), pygame.Rect(0,450,800,75))





pygame.draw.rect(screen, (0, 74, 193), pygame.Rect(0,0,800,75))
pygame.draw.rect(screen, (15, 84, 196), pygame.Rect(0,75,800,65))
pygame.draw.rect(screen, (31, 95, 198), pygame.Rect(0,140,800,55))
pygame.draw.rect(screen, (56, 107, 188), pygame.Rect(0,195,800,45))
pygame.draw.rect(screen, (84, 125, 188), pygame.Rect(0,240,800,35))
pygame.draw.rect(screen, (110, 136, 178), pygame.Rect(0,275,800,25))


pygame.display.flip ()
