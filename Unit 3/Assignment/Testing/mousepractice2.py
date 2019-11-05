import pygame

pygame.init()
size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)

# Define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)

# Creates a rectangle for the indicator box
indicator = pygame.Rect (200, 100, 100, 100)
indicator2 = pygame.Rect (400, 300, 300, 300)
indicator3 = pygame.Rect (200, 500, 100, 500)

mousehistory = 0
screen.fill (WHITE)


def menu(m):
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

#Main loop that checks events
while running:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False                   
    mx, my, mb = getmouse()
    
    menu(mousehistory)

    pygame.display.flip()
    

pygame.quit()