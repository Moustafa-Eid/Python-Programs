# Name: Moustafa Eid
# Date: March 13th 2017
# Class: ICS3U1-03
# Description: Animation of a Tic Tac Toe Game

import pygame

#setting up pygame and screen
pygame.init() 
SIZE = (600, 600) 
screen = pygame.display.set_mode(SIZE)

# Changes Screen Background to White
pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,600,600))

# Draws Grid for Tic Tac Toe
pygame.draw.line(screen, (0,0,0), (0,200), (600,200))
pygame.draw.line(screen, (0,0,0), (0,400), (600,400))
pygame.draw.line(screen, (0,0,0), (200,0), (200,600))
pygame.draw.line(screen, (0,0,0), (400,0), (400,600))
pygame.display.flip()
pygame.time.wait(1000)

# Draws First Move [X]
pygame.draw.line(screen, (0,0,0), (25,25), (175,175))
pygame.draw.line(screen, (0,0,0), (175,25), (25,175))                         
pygame.display.flip()
pygame.time.wait(1000)

# Draws Second Move [O]
pygame.draw.circle(screen, (0,0,0), (300,300), 85,1)
pygame.display.flip()
pygame.time.wait(1000)

# Draws Third Move [X]
pygame.draw.line(screen, (0,0,0), (425,425), (575,575))
pygame.draw.line(screen, (0,0,0), (575,425), (425,575))                         
pygame.display.flip()
pygame.time.wait(1000)

# Draws Fourth Move [O]
pygame.draw.circle(screen, (0,0,0), (500,100), 85,1)
pygame.display.flip()
pygame.time.wait(1000)

# Draws Fifth Move [X]
pygame.draw.line(screen, (0,0,0), (25,425), (175,575))
pygame.draw.line(screen, (0,0,0), (175,425), (25,575))                         
pygame.display.flip()
pygame.time.wait(1000)

# Draws Sixth Move [O]
pygame.draw.circle(screen, (0,0,0), (100,300), 85,1)
pygame.display.flip()
pygame.time.wait(1000)

# Draws Seventh Move [X]
pygame.draw.line(screen, (0,0,0), (225,425), (375,575))
pygame.draw.line(screen, (0,0,0), (375,425), (225,575))                         
pygame.display.flip()
pygame.time.wait(1000)

# Draws Line Indicating Winner
pygame.draw.line(screen, (0,0,0), (0,500), (600,500))                         
pygame.display.flip()
pygame.time.wait(3000)
