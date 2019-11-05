# Name: Moustafa Eid
# Date: April 12 2017
# Class: ICS3U1-03
# Description: Assignment - Draw house with detailed random background

import pygame
import math
import random

#setting up pygame and screen
pygame.init() 
SIZE = (800, 600) 
screen = pygame.display.set_mode(SIZE)
#Jelly Fish Pos
x1 = random.randint(0,600)
y1 = random.randint(0,500)
x2 = random.randint(0,600)
y2 = random.randint(0,500)
x3 = random.randint(0,600)
y3 = random.randint(0,500)
# Plants Pos
x4 = random.randint(0,280)
y4 = random.randint(500,600)
x5 = random.randint(0,280)
y5 = random.randint(500,600)
x6 = random.randint(0,280)
y6 = random.randint(500,600)
x7 = random.randint(0,280)
y7 = random.randint(500,600)
x8 = random.randint(600,800)
y8 = random.randint(500,600)
x11 = random.randint(600,800)
y11 = random.randint(500,600)
x12 = random.randint(600,800)
y12 = random.randint(500,600)
x13 = random.randint(600,800)
y13 = random.randint(500,600)
x14 = random.randint(600,800)
y14 = random.randint(500,600)

#Windows Pos
y9 = random.randint(300,450)
y10 = random.randint(300,450)

pygame.display.flip ()
# Functions for repeated drawings
def roundplant (x,y):
    pygame.draw.circle(screen, (207,97,189), (x,y),20)
    pygame.draw.rect(screen, (229,239,210), pygame.Rect(x-20,y+5,40,20))
def straightplant (x,y):
    pygame.draw.line(screen, (64,91,12),(x,y),(x,y-30),2)
    pygame.draw.line(screen, (64,91,12),(x,y-20),(x-20,y-25),2)
    pygame.draw.line(screen, (64,91,12),(x,y-20),(x+20,y-25),2)
    pygame.draw.line(screen, (64,91,12),(x-20,y-25),(x-22,y-10),2)
    pygame.draw.line(screen, (64,91,12),(x+20,y-25),(x+22,y-10),2)
def jellyfish (x,y):
    pygame.draw.circle(screen, (237,162,185), (x,y),25)
    pygame.draw.rect(screen, (237,162,185), pygame.Rect(x-25,y+4,50,20))
    pygame.draw.line(screen, (237,162,185),(x-20,y+24),(x-20,y+50),2)
    pygame.draw.line(screen, (237,162,185),(x-5,y+24),(x-5,y+50),2)
    pygame.draw.line(screen, (237,162,185),(x+10,y+24),(x+10,y+50),2)
    pygame.draw.line(screen, (237,162,185),(x+20,y+24),(x+20,y+50),2)    

#Background of Picture (Sky And Sand)
pygame.draw.rect(screen, (110, 136, 178), pygame.Rect(0,0,800,85))
pygame.draw.rect(screen, (84, 125, 188), pygame.Rect(0,85,800,80))
pygame.draw.rect(screen, (56, 107, 188), pygame.Rect(0,165,800,75))
pygame.draw.rect(screen, (31, 95, 198), pygame.Rect(0,240,800,70))
pygame.draw.rect(screen, (15, 84, 196), pygame.Rect(0,310,800,65))
pygame.draw.rect(screen, (0, 74, 193), pygame.Rect(0,375,800,60))
pygame.draw.rect(screen, (229,239,210), pygame.Rect(0,435,800,165))

pygame.display.flip ()
# House Outline
pygame.draw.ellipse(screen,(247,178,44), pygame.Rect(300,150,270,400))
pygame.draw.rect(screen, (229,239,210), pygame.Rect(0,500,800,165))
pygame.draw.rect(screen, (84, 125, 188), pygame.Rect(0,85,800,80))

# Diagonal Lines
pygame.draw.line(screen, (207,94,12),(331,221),(435,165),2)
pygame.draw.line(screen, (207,94,12),(309,277),(485,165),2)
pygame.draw.line(screen, (207,94,12),(300,333),(515,190),2)
pygame.draw.line(screen, (207,94,12),(303,389),(540,225),2)
pygame.draw.line(screen, (207,94,12),(317,445),(558,270),2)
pygame.draw.line(screen, (207,94,12),(345,500),(570,330),2)
# opposite Diagonal Lines
pygame.draw.line(screen, (207,94,12),(539,221),(435,165),2)    
pygame.draw.line(screen, (207,94,12),(561,277),(385,165),2)
pygame.draw.line(screen, (207,94,12),(570,333),(355,190),2)
pygame.draw.line(screen, (207,94,12),(567,389),(330,225),2)
pygame.draw.line(screen, (207,94,12),(553,445),(312,270),2)
pygame.draw.line(screen, (207,94,12),(525,500),(300,330),2)


#Door
pygame.draw.circle(screen, (188,211,250), (435,425),35)
pygame.draw.circle(screen, (70,99,176), (435,425),35,2)
pygame.draw.rect(screen, (188,211,250), pygame.Rect(400,420,70,80))
pygame.draw.rect(screen, (70,99,176), pygame.Rect(400,420,70,80),2)
pygame.draw.line(screen, (188,211,250),(402,420),(468,420),2)
pygame.draw.circle(screen, (70,99,176), (435,425),25,2)
pygame.draw.rect(screen, (188,211,250), pygame.Rect(410,420,50,80))
pygame.draw.rect(screen, (70,99,176), pygame.Rect(410,420,50,80),2)
pygame.draw.line(screen, (188,211,250),(412,420),(458,420),2)
pygame.draw.circle(screen, (70,99,176), (435,425),15,2)
pygame.draw.rect(screen, (188,211,250), pygame.Rect(420,420,30,70))
pygame.draw.rect(screen, (70,99,176), pygame.Rect(420,420,30,70),2)
pygame.draw.line(screen, (188,211,250),(422,420),(448,420),2)
pygame.draw.circle(screen, (70,99,176), (435,455),2,2)
pygame.draw.circle(screen, (70,99,176), (435,455),5,2)
pygame.draw.circle(screen, (70,99,176), (435,455),8,2)
pygame.draw.circle(screen, (70,99,176), (435,455),10,2)




#Windows
pygame.draw.circle(screen, (149,186,245), (360,y9),30)
pygame.draw.circle(screen, (70,99,176), (360,y9),30,2)
pygame.draw.circle(screen, (182,236,254), (360,y9),20)
pygame.draw.circle(screen, (70,99,176), (360,y9),20,2)

pygame.draw.circle(screen, (149,186,245), (510,y10),30)
pygame.draw.circle(screen, (70,99,176), (510,y10),30,2)
pygame.draw.circle(screen, (182,236,254), (510,y10),20)
pygame.draw.circle(screen, (70,99,176), (510,y10),20,2)

#Chimney
pygame.draw.polygon(screen, (82,113,194), [[540, 240], [540, 250],[580, 250],[580,215],[585,200],[565,200],[570,215],[570,240]])
pygame.draw.polygon(screen, (25,72,148), [[540, 240], [540, 250],[580, 250],[580,215],[585,200],[565,200],[570,215],[570,240]],2)
pygame.draw.line(screen, (25,72,148),(570,215),(580,215),2)


#Leaves
pygame.draw.polygon(screen, (90,153,42), [[385, 163], [345, 123],[525, 123],[485,164]])
pygame.draw.polygon(screen, (84, 125, 188), [[430, 123], [435, 143],[440, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[420, 123], [425, 143],[430, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[410, 123], [415, 143],[420, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[400, 123], [405, 143],[410, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[390, 123], [395, 143],[400, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[380, 123], [385, 143],[390, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[345, 123], [375, 143],[380, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[440, 123], [445, 143],[450, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[450, 123], [455, 143],[460, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[460, 123], [465, 143],[470, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[470, 123], [475, 143],[480, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[480, 123], [485, 143],[490, 123]])
pygame.draw.polygon(screen, (84, 125, 188), [[490, 123], [495, 143],[525, 123]])

#Pathway
pygame.draw.polygon(screen, (86,115,104), [[400, 500], [470, 500],[600, 800],[270,800]])
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(440,500,20,10))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(410,500,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(400,515,20,10))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(425,515,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(450,510,20,10))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(450,525,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(425,533,20,10))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(395,530,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(455,543,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(425,545,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(395,548,20,10))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(425,563,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(460,562,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(395,562,20,10))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(425,580,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(395,580,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(455,580,25,15))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(375,575,20,10))
pygame.draw.ellipse(screen,(159,192,126), pygame.Rect(480,575,20,10))

#Plants Round
roundplant (x4,y4)
roundplant (x5,y5)
roundplant (x6,y6)
roundplant (x7,y7)


# Plants
straightplant (x8,y8)
straightplant (x11,y11)
straightplant (x12,y12)
straightplant (x13,y13)
straightplant (x14,y14)

# JellyFish
jellyfish (x1,y1)
jellyfish (x2,y2)
jellyfish (x3,y3)
jellyfish (x4,y4)
pygame.display.flip ()
