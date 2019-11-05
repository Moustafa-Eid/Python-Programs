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


##Checking for collision detection 
#def drawScene(screen, mx, my): 
    ## If mouse is within BOTH the x AND y ranges of the box, then collision has occurred
    #if indicator.collidepoint(mx,my) and mb == 0:
        #pygame.draw.rect(screen, RED, indicator, 0)     
    #else:
        #pygame.draw.rect(screen, GREEN, indicator, 0)
    
    #if indicator2.collidepoint(mx,my) and mb == 0:
        #pygame.draw.rect(screen, RED, indicator2, 0)
    #else:
        #pygame.draw.rect(screen, GREEN, indicator2, 0)
        
    #if indicator3.collidepoint(mx,my) and mb == 0:
        #pygame.draw.rect(screen, RED, indicator3, 0)
    #else:
        #pygame.draw.rect(screen, GREEN, indicator3, 0)
   
            


##Function to check if the user has clicked on a box     
#def mouseClick(screen, mx, my, mb):
    #if indicator.collidepoint(mx,my) and mb == 1:
        ##pygame.draw.rect(screen, BLUE, pygame.Rect (0,0,800,600), 0)
        #screen.fill(BLUE)
        #mousehistory = 1
    #if indicator2.collidepoint(mx,my) and mb == 1:
        ##pygame.draw.rect(screen, BLUE, pygame.Rect (0,0,800,600), 0)
        #screen.fill(BLUE)
        #mousehistory = 1
    #if indicator3.collidepoint(mx,my) and mb == 1:
        ##pygame.draw.rect(screen, BLUE, pygame.Rect (0,0,800,600), 0) 
        #screen.fill(BLUE)
        #mousehistory = 1
    #pygame.display.flip()
    
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

    if mousehistory == 0:
        pygame.draw.rect(screen, GREEN, indicator, 0)
        pygame.draw.rect(screen, GREEN, indicator2, 0)
        pygame.draw.rect(screen, GREEN, indicator3, 0)
        
        if indicator.collidepoint(mx,my):
            if mb == 0:
                pygame.draw.rect(screen, RED, indicator, 0)
            if mb == 1:
                screen.fill(BLUE)
                mousehistory = 1                
        if indicator2.collidepoint(mx,my):
            if mb == 0:            
                pygame.draw.rect(screen, RED, indicator2, 0)
            if mb == 1:
                screen.fill(BLUE)
                mousehistory = 1             
        if indicator3.collidepoint(mx,my):
            if mb == 0:
                pygame.draw.rect(screen, RED, indicator3, 0)
            if mb == 1:
                screen.fill(BLUE)
                mousehistory = 1
    elif mousehistory == 1:
        screen.fill(BLUE)
        
    pygame.display.flip()
    

pygame.quit()