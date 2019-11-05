import pygame
import time
import math
pygame.init()
size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)

# Define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)

fontmenu = pygame.font.SysFont("French Script MT Regular",60)
fontvirus = pygame.font.SysFont("Arial",28)
fontback = pygame.font.SysFont("Times New Roman",50)


# Creates a rectangle for the indicator box
indicator = pygame.Rect(260,150,320,37)
indicator2 = pygame.Rect (260, 300, 333, 37)
indicator3 = pygame.Rect (360, 450, 87, 37)

virus1 = pygame.Rect (20,100,320,40)
virus2 = pygame.Rect (20,130,320,40)
virus3 = pygame.Rect (20,160,320,40)
virus4 = pygame.Rect (20,190,320,40)
virus5 = pygame.Rect (20,220,320,40)
virus6 = pygame.Rect (20,250,320,40)
virus7 = pygame.Rect (20,280,320,40)
virus8 = pygame.Rect (20,310,320,40)
virus9 = pygame.Rect (20,340,320,40)
virus10 = pygame.Rect (20,370,320,40)


crime = pygame.Rect (250,300,320,40)
back = pygame.Rect (5,540,103,47)

mousehistory = 0
menuopt = 0

canvas_width = 800
canvas_height = 600
color = pygame.Color(255, 255, 0, 0)
background_color = pygame.Color(0, 0, 0, 0)

screen.fill (WHITE)

def textvirus():
    textvirus1 = fontvirus.render("A Trojan virus is a virus that is sent to your computer via a hidden program. " , 1, WHITE)
    screen.blit(textvirus1, virus1)
    textvirus2 = fontvirus.render("A Trojan disguises itself as an important program to make you believe it's " , 1, WHITE)
    screen.blit(textvirus2, virus2)
    textvirus3 = fontvirus.render("safe. A Trojan virus usually plants itseld in highly desireable downloads " , 1, WHITE)
    screen.blit(textvirus3, virus3)
    textvirus4 = fontvirus.render("such as Games, Movies, Music and any Freeware. Trojans do not multiply" , 1, WHITE)
    screen.blit(textvirus4, virus4)
    textvirus5 = fontvirus.render("or spread like other viruses. However they are very dangerous because" , 1, WHITE)
    screen.blit(textvirus5, virus5)
    textvirus6 = fontvirus.render("they can record your login input and send it to hackers worldwide." , 1, WHITE)
    screen.blit(textvirus6, virus6)
    textvirus7 = fontvirus.render("Trojan Viruses are highly used among cyber thieves to steal your" , 1, WHITE)
    screen.blit(textvirus7, virus7)
    textvirus8 = fontvirus.render("financial information and personal data. To avoid trojans do not" , 1, WHITE)
    screen.blit(textvirus8, virus8)
    textvirus9 = fontvirus.render("download any files from untrusted sources and websites." , 1, WHITE)
    screen.blit(textvirus9, virus9)
    textvirus10 = fontvirus.render("An Example of a Trojan virus is ZeuS" , 1, WHITE)
    screen.blit(textvirus10, virus10)
    
def menu():
    global mousehistory, mb, mx, my, menuopt, running
    if mousehistory == 0:
        text1 = fontmenu.render("Computer Virus" , 1, GREEN)
        screen.blit(text1, indicator)
        text2 = fontmenu.render("Computer Crime" , 1, GREEN)
        screen.blit(text2, indicator2)        
        text3 = fontmenu.render("Quit" , 1, GREEN)
        screen.blit(text3, indicator3)    
        if indicator.collidepoint(mx,my) and mousehistory == 0:
            if mb == 0:
                text1 = fontmenu.render("Computer Virus" , 1, RED)
                screen.blit(text1, indicator)
            if mb == 1:
                mousehistory = 1
                menuopt = 1                 
        if indicator2.collidepoint(mx,my) and mousehistory == 0:
            if mb == 0:            
                text2 = fontmenu.render("Computer Crime" , 1, RED)
                screen.blit(text2, indicator2)
            if mb == 1:              
                mousehistory = 1
                menuopt = 2
        if indicator3.collidepoint(mx,my) and mousehistory == 0:
            if mb == 0:
                text3 = fontmenu.render("Quit" , 1, RED)
                screen.blit(text3, indicator3)
            if mb == 1:
                mousehistory = 1
                menuopt = 3
    if mousehistory == 1:
        if menuopt == 1 and mousehistory == 1:
            screen.fill(BLUE)
            textvirus()
            textback = fontback.render("Back" , 1, GREEN)
            screen.blit(textback, back)
            if back.collidepoint(mx,my):                 
                if mb == 0:
                    textback = fontback.render("Back" , 1, RED)
                    screen.blit(textback, back)
                if mb == 1:
                    screen.fill (WHITE)
                    mousehistory = 0
        if menuopt == 2 and mousehistory == 1:
            screen.fill(BLUE)
            textcrime = fontmenu.render("Computer Crime" , 1, RED)
            screen.blit(textcrime, crime)
            textback = fontback.render("Back" , 1, GREEN)
            screen.blit(textback, back)
            if back.collidepoint(mx,my):                 
                if mb == 0:
                    textback = fontback.render("Back" , 1, RED)
                    screen.blit(textback, back)
                if mb == 1:
                    screen.fill (WHITE)
                    mousehistory = 0            
        if menuopt == 3 and mousehistory == 1:
            running = False    
    
    
#Getting mouse cordinates 
def getmouse():
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()[0]
    return (mx, my, mb)

running = True
myClock = pygame.time.Clock()

#Main loop that checks events
while running:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False                   
    mx, my, mb = getmouse()
    screen.fill (BLACK)
    frequency = 4
    amplitude = 50 # in px
    speed = 1
    for x in range(0, canvas_width):
        y = int((canvas_height/2) + amplitude*math.sin(frequency*((float(x)/canvas_width)*(2*math.pi) + (speed*time.time()))))
        screen.set_at((x, y), color)
    screen.blit(screen, (0, 0))    
    menu()
    pygame.display.flip()
    myClock.tick(1000)
    

pygame.quit()