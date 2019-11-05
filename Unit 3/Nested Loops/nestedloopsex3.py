import pygame

pygame.init()
size = (width, height) = (765, 765)
screen = pygame.display.set_mode(size)

# Define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
GREY = (142,143,147)
BROWN = (170,83,1)

x1 = 0
y1 = 765
x2 = 0
y2 = 764

R = 0
G = 255
B = 0

for count in range(3):
    if G == 255 and R == 0:
        for colour in range (255):
            pygame.draw.line (screen,(R,G,B), (x1,y1) , (x2,y2), 1)
            pygame.display.flip()            
            G -= 1
            R += 1
            x1 += 1
            x2 += 1
            y2 -= 1            
    if G == 0 and R == 255:
        for colour in range (255):
            pygame.draw.line (screen,(R,G,B), (x1,y1) , (x2,y2), 1)
            pygame.display.flip()            
            G += 1
            R -= 1
            x1 += 1
            x2 += 1
            y2 -= 1            
            
    