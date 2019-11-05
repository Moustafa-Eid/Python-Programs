# Name: Moustafa Eid
# Date: March 13th 2017
# Class: ICS3U1-03
# Description: Animation of a Tic Tac Toe Game

import pygame
import math

#setting up pygame and screen
pygame.init() 
SIZE = (800, 800) 
screen = pygame.display.set_mode(SIZE)

## Makes the setting and scenery
#pygame.draw.rect(screen, (244,205,162), pygame.Rect(0,300,800,600))
#pygame.draw.rect(screen, (109,207,244), pygame.Rect(0,0,800,300))
pygame.draw.rect(screen, (246,178,75), pygame.Rect(0,0,800,800))
pygame.display.flip ()


pygame.draw.ellipse(screen, (255,255,255), [350,100,250,200])
pygame.draw.circle(screen, (255,255,255), (460,370), 200)

pygame.draw.arc(screen, (246,178,75), [400,95,150,50], 2*math.pi/2, 2*math.pi, 3)
pygame.draw.arc(screen, (170,171,175), [430,80,100,50], 2*math.pi/2, 2*math.pi, 15) 

pygame.draw.circle(screen, (0,0,0), (480,130), 23)
pygame.draw.circle(screen, (255,255,255), (475,125), 8)

pygame.draw.line(screen, (0,0,0), (560,125), (580,100),5)
pygame.draw.line(screen, (255,255,255), (580,100), (600,70),5)
pygame.draw.line(screen, (255,255,255), (540,125), (575,70),5)

pygame.draw.circle(screen, (170,171,175), (530,160), 17,2)
pygame.draw.circle(screen, (0,0,0), (530,160), 14)
pygame.draw.circle(screen, (255,255,255), (528,155), 5)

pygame.draw.circle(screen, (246,178,75), (460,370), 130,50)
pygame.draw.circle(screen, (170,171,175), (460,370), 100,5)
pygame.draw.circle(screen, (170,171,175), (460,370), 40)
pygame.draw.line(screen, (255,255,255), (480,310), (440,410),2)
pygame.draw.line(screen, (255,255,255), (460,310), (420,410),2)
pygame.draw.line(screen, (255,255,255), (500,310), (460,410),2)
pygame.draw.circle(screen, (246,178,75), (250,375), 70)
pygame.draw.circle(screen, (246,178,75), (675,375), 70)
pygame.draw.circle(screen, (246,178,75), (460,585), 70)

#pygame.draw.circle(screen, (244,205,162), (190,375), 70)
#pygame.draw.circle(screen, (244,205,162), (230,354), 30)
#pygame.draw.circle(screen, (244,205,162), (232,345), 30)
#pygame.draw.circle(screen, (244,205,162), (255,330), 10)
#pygame.draw.line(screen, (244,205,162), (190,315), (263,315),30)

pygame.draw.circle(screen, (195,186,178), (460,370), 200,4)

pygame.display.flip ()
