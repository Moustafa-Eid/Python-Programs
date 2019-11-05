# Name: Moustafa Eid
# Date: March 13th 2017
# Class: ICS3U1-03
# Description: Animation of a Tic Tac Toe Game

import pygame

xpos = int(input("Please Enter The X Position: "))
ypos = int(input("Please Enter The Y Position: "))
#setting up pygame and screen
pygame.init() 
SIZE = (400, 300) 
screen = pygame.display.set_mode(SIZE)

# Changes Screen Background to White
pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,400,300))

#Function For Drawing Cube
def cube (x,y):
    pygame.draw.line (screen,(0,0,0),(x,y),(x,y+20),2)
    pygame.draw.line (screen,(0,0,0),(x,y),(x+20,y),2)
    pygame.draw.line (screen,(0,0,0),(x,y),(x+10,y-10),2)
    pygame.draw.line (screen,(0,0,0),(x+20,y),(x+20,y+20),2)
    pygame.draw.line (screen,(0,0,0),(x+20,y),(x+30,y-10),2)
    pygame.draw.line (screen,(0,0,0),(x+10,y-10),(x+30,y-10),2)
    pygame.draw.line (screen,(0,0,0),(x+30,y-10),(x+30,y+10),2)
    pygame.draw.line (screen,(0,0,0),(x+30,y+10),(x+20,y+20),2)
    pygame.draw.line (screen,(0,0,0),(x,y+20),(x+20,y+20),2)
    


# Draw Cube 
cube (xpos,ypos)
pygame.display.flip()