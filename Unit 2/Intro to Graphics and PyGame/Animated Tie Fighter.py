# Name: Moustafa Eid
# Date: March 23rd 2017
# Class: ICS3U1-03
# Description: Art Show Picture
import pygame
import math

#setting up pygame and screen
pygame.init() 
SIZE = (800, 700) 
screen = pygame.display.set_mode(SIZE)
speed = 15
# Draws the setting and scenery

pygame.display.flip ()

for count in range(800):
    pygame.draw.rect(screen, (244,205,162), pygame.Rect(0,300,800,500))
    pygame.draw.rect(screen, (0, 74, 193), pygame.Rect(0,0,800,75))
    pygame.draw.rect(screen, (15, 84, 196), pygame.Rect(0,75,800,65))
    pygame.draw.rect(screen, (31, 95, 198), pygame.Rect(0,140,800,55))
    pygame.draw.rect(screen, (56, 107, 188), pygame.Rect(0,195,800,45))
    pygame.draw.rect(screen, (84, 125, 188), pygame.Rect(0,240,800,35))
    pygame.draw.rect(screen, (110, 136, 178), pygame.Rect(0,275,800,25))
    pygame.draw.circle(screen, (252, 212, 64), (200,100),70)
    pygame.draw.circle(screen, (252, 212, 64), (70,200),30)
    pygame.draw.circle(screen, (255,255,255), (500,90),30)
    pygame.draw.circle(screen, (255,255,255), (530,60),30)
    pygame.draw.circle(screen, (255,255,255), (530,85),30)
    pygame.draw.circle(screen, (255,255,255), (550,60),30)
    pygame.draw.circle(screen, (255,255,255), (550,85),30)
    pygame.draw.circle(screen, (255,255,255), (570,75),30)
    pygame.draw.circle(screen, (255,255,255), (570,85),30)
    pygame.draw.circle(screen, (255,255,255), (590,60),30)
    pygame.draw.circle(screen, (255,255,255), (590,85),30)
    pygame.draw.circle(screen, (255,255,255), (620,90),30)    
    
    
    pygame.draw.polygon(screen, (183,187,193), [[800-(count*speed), 270], [800-((count*speed)-10), 250],[800-(count*speed), 230],[800-((count*speed)+20),235],[800-((count*speed)+30),255],[800-((count*speed)+20),275]])
    pygame.draw.polygon(screen, (0,0,0), [[800-((count*speed)+2), 268], [800-((count*speed)-8), 250],[800-((count*speed)+2), 232],[800-((count*speed)+18),237],[800-((count*speed)+28),255],[800-((count*speed)+18),273]])
    pygame.draw.circle(screen, (183,187,193), (800-((count*speed)+11),255),5)    
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)+11), 255),(800-((count*speed)+2),268),3)
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)+11), 255),(800-((count*speed)-8),250),3)
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)+11), 255),(800-((count*speed)+2),232),3)
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)+11), 255),(800-((count*speed)+18),237),3)
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)+11), 255),(800-((count*speed)+28),255),3)
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)+11), 255),(800-((count*speed)+18),273),3)
    pygame.draw.polygon(screen, (73,75,77), [[800-((count*speed)+11), 255], [800-((count*speed)+10), 253],[800-((count*speed)-10), 247],[800-((count*speed)-10),256]])
    pygame.draw.circle(screen, (142,143,147), (800-((count*speed)-10),255),10)
    pygame.draw.circle(screen, (0,0,0), (800-((count*speed)-7),255),5)
    pygame.draw.circle(screen, (142,143,147), (800-((count*speed)-7),255),2,2)
    pygame.draw.polygon(screen, (73,75,77), [[800-((count*speed)-20), 247], [800-((count*speed)-26), 250],[800-((count*speed)-26), 253],[800-((count*speed)-22),256]])
    
    pygame.draw.polygon(screen, (183,187,193), [[800-((count*speed)-32), 275], [800-((count*speed)-22), 255],[800-((count*speed)-32), 235],[800-((count*speed)-52),230],[800-((count*speed)-62),250],[800-((count*speed)-52),270]])
    pygame.draw.polygon(screen, (0,0,0), [[800-((count*speed)-34), 273], [800-((count*speed)-24), 255],[800-((count*speed)-34), 237],[800-((count*speed)-50),232],[800-((count*speed)-60),250],[800-((count*speed)-50),268]])
            
    pygame.draw.circle(screen, (183,187,193), (800-((count*speed)-40),255),5)
    
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)-40), 255),(800-((count*speed)-34),273),3)
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)-40), 255),(800-((count*speed)-24),255),3)
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)-40), 255),(800-((count*speed)-34),237),3)
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)-40), 255),(800-((count*speed)-50),232),3)
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)-40), 255),(800-((count*speed)-60),250),3)
    pygame.draw.line (screen, (183,187,193),(800-((count*speed)-40), 255),(800-((count*speed)-50),268),3)
    
    pygame.display.flip ()
    pygame.time.wait(100)
