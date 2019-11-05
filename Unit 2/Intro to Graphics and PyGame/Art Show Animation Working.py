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
speed = 30
# Draws the setting and scenery

pygame.display.flip ()

while (True):
    for count in range(40):
        pygame.draw.rect(screen, (244,205,162), pygame.Rect(0,300,800,500))
        pygame.draw.rect(screen, (0, 74, 193), pygame.Rect(0,0,800,75))
        pygame.draw.rect(screen, (15, 84, 196), pygame.Rect(0,75,800,65))
        pygame.draw.rect(screen, (31, 95, 198), pygame.Rect(0,140,800,55))
        pygame.draw.rect(screen, (56, 107, 188), pygame.Rect(0,195,800,45))
        pygame.draw.rect(screen, (84, 125, 188), pygame.Rect(0,240,800,35))
        pygame.draw.rect(screen, (110, 136, 178), pygame.Rect(0,275,800,25))
        
        # Sun and Moon
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
           
        # Tie Fighter
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
        
       
        # A-Wing
        pygame.draw.ellipse(screen, (0,0,0), pygame.Rect(800-((count*speed)-200),250,20,10))
        pygame.draw.rect(screen, (243,88,87), pygame.Rect(800-((count*speed)-200),255,50,15))
        pygame.draw.ellipse(screen, (243,88,87), pygame.Rect(800-((count*speed)-173),254,50,17))
        pygame.draw.rect(screen, (243,88,87), pygame.Rect(800-((count*speed)-170),260,10,5))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(800-((count*speed)-200),265,50,5))
        pygame.draw.ellipse(screen, (255,255,255), pygame.Rect(800-((count*speed)-200),262,20,10))
        pygame.draw.ellipse(screen, (255,255,255), pygame.Rect(800-((count*speed)-210),262,20,10))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(800-((count*speed)-220),260,20,5))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(800-((count*speed)-240),255,10,10))
        pygame.draw.polygon(screen, (255,255,255), [[800-((count*speed)-250),255],[800-((count*speed)-255),250],[800-((count*speed)-260),250],[800-((count*speed)-260),255]])
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(800-((count*speed)-250),255,10,15))
        pygame.draw.line(screen, (161,165,178),(800-((count*speed)-257),255),(800-((count*speed)-257),269),5)    
    
        
        # Head And Body Outlines
        pygame.draw.circle (screen, (255,255,255), (400,300), 100)
        pygame.draw.rect(screen, (244,205,162), pygame.Rect(0,300,800,550))
        pygame.draw.circle(screen, (0,0,0), (400,470),171,1)
        pygame.draw.circle(screen, (255,255,255), (400,470),170)
        
        #Drawing Head Features
        
        #Eyes    
        pygame.draw.circle(screen, (244,139,42), (400,655),60)
        pygame.draw.circle(screen, (255,255,255), (400,650),40)
        
        #Neck
        pygame.draw.polygon(screen, (255,255,255), [[300, 300], [350, 313],[450, 313],[500,300]])
        pygame.draw.polygon(screen, (0,0,0), [[300, 300], [350, 313],[450, 313],[500,300]],1)
        
        #Outer Outline
        pygame.draw.line(screen,(115,121,126), (300,296) , (500,296),7)
        pygame.draw.line(screen,(0,0,0), (300,292) , (500,292),1)
        
        #Sensor
        pygame.draw.circle(screen,(0,0,0),(400,277),8,1)
        pygame.draw.circle(screen,(0,0,0),(400,277),6,1)
        pygame.draw.circle(screen,(0,0,0),(400,240),20)
        pygame.draw.circle(screen,(65,70,74),(400,240),25,5)
        pygame.draw.circle(screen,(0,0,0),(450,265),10)
        pygame.draw.circle(screen,(65,70,74),(450,265),11,3)
        pygame.draw.circle(screen,(65,70,74),(450,265),15,2)
        
        #Drawing Head Design
        pygame.draw.line(screen,(244,139,42), (420,218) , (450,218),7)
        pygame.draw.line(screen,(244,139,42), (350,218) , (380,218),7)
        pygame.draw.line(screen,(65,70,74), (370,207) , (430,207),7)
        pygame.draw.circle(screen,(65,70,74),(432,207),4)
        pygame.draw.circle(screen,(65,70,74),(368,207),4)
        pygame.draw.line(screen,(0,0,0), (410,200) , (410,193),2)
        pygame.draw.line(screen,(255,255,255), (410,193) , (410,150),2)
        pygame.draw.line(screen,(0,0,0), (410,150) , (410,145),2)
        pygame.draw.line(screen,(255,255,255), (390,200) , (390,178),2)
        pygame.draw.rect(screen, (244,139,42), pygame.Rect(360,277,10,15))
        pygame.draw.rect(screen, (244,139,42), pygame.Rect(330,277,25,15))
        pygame.draw.rect(screen, (244,139,42), pygame.Rect(315,277,10,15))
        pygame.draw.rect(screen, (244,139,42), pygame.Rect(300,277,10,15))
        pygame.draw.line(screen,(6,187,220), (343,283) , (352,283),3)
        pygame.draw.line(screen,(6,187,220), (343,287) , (352,287),3)
        pygame.draw.rect(screen, (244,139,42), pygame.Rect(455,284,8,8))
        pygame.draw.rect(screen, (244,139,42), pygame.Rect(470,277,20,15))
        pygame.draw.rect(screen, (244,139,42), pygame.Rect(492,277,2,15))
        pygame.draw.rect(screen, (244,139,42), pygame.Rect(495,277,2,15))
        
        #Drawing body Features
        
        # Middle Circle
        pygame.draw.circle(screen, (244,139,42), (400,470),100,35)
        pygame.draw.circle(screen, (149,160,163), (400,470),42)
        pygame.draw.polygon(screen, (244,139,42), [[315, 460], [345, 460],[345, 480],[315,480]])
        pygame.draw.polygon(screen, (244,139,42), [[390, 385], [390, 415],[410, 415],[410,385]])
        pygame.draw.polygon(screen, (244,139,42), [[485, 460], [455, 460],[455, 480],[485,480]])
        pygame.draw.polygon(screen, (244,139,42), [[390, 555], [390, 525],[410, 525],[410,555]])
        pygame.draw.circle(screen, (164,89,36), (335,470),7,1)
        pygame.draw.circle(screen, (164,89,36), (335,470),4,1)
        pygame.draw.circle(screen, (164,89,36), (465,470),7,1)
        pygame.draw.circle(screen, (164,89,36), (465,470),4,1)
        pygame.draw.circle(screen, (164,89,36), (400,405),7,1)
        pygame.draw.circle(screen, (164,89,36), (400,405),4,1)
        pygame.draw.circle(screen, (164,89,36), (400,535),7,1)
        pygame.draw.circle(screen, (164,89,36), (400,535),4,1)
        pygame.draw.circle(screen, (244,139,42), (215,470),60)
        pygame.draw.circle(screen, (255,255,255), (220,470),40)
        pygame.draw.circle(screen, (149,160,163), (225,470),20)
        
        #Drawing Outer Circles and Layering arc om top of outer edges to hide
        #Left Circle
        pygame.draw.arc(screen, (244,205,162), [148,235,470,470], 2.35619, 3.92699, 80)
        pygame.draw.circle(screen, (0,0,0), (400,470),171,1)
        pygame.draw.polygon(screen, (255,255,255), [[300, 300], [350, 313],[450, 313],[500,300]])
        pygame.draw.polygon(screen, (0,0,0), [[300, 300], [350, 313],[450, 313],[500,300]],1)
        pygame.draw.circle(screen, (244,139,42), (585,470),60)
        pygame.draw.circle(screen, (255,255,255), (580,470),40)
        pygame.draw.circle(screen, (149,160,163), (575,470),20)    
    
        # Right Circle
        pygame.draw.arc(screen, (244,205,162), [180,230,470,480],5.49779,7.06858, 80)
        pygame.draw.circle(screen, (0,0,0), (400,470),171,1)
        pygame.draw.polygon(screen, (255,255,255), [[300, 300], [350, 313],[450, 313],[500,300]])
        pygame.draw.polygon(screen, (0,0,0), [[300, 300], [350, 313],[450, 313],[500,300]],1)
        pygame.draw.circle(screen, (244,139,42), (400,655),60)
        pygame.draw.circle(screen, (255,255,255), (400,650),40)
        pygame.draw.circle(screen, (149,160,163), (400,645),20)
        
        #Bottom Circle
        pygame.draw.arc(screen, (244,205,162), [160,250,480,470],3.92699,5.49779, 80)
        pygame.draw.circle(screen, (0,0,0), (400,470),171,1)
        pygame.draw.polygon(screen, (255,255,255), [[300, 300], [350, 313],[450, 313],[500,300]])
        pygame.draw.polygon(screen, (0,0,0), [[300, 300], [350, 313],[450, 313],[500,300]],1)
        pygame.draw.circle(screen, (149,160,163), (295,428),5)
        pygame.draw.circle(screen, (149,160,163), (295,513),5)
        
        # Drawing Circles around middle
        pygame.draw.circle(screen, (149,160,163), (350,575),5)
        pygame.draw.circle(screen, (149,160,163), (350,365),5)
        pygame.draw.circle(screen, (149,160,163), (505,428),5)
        pygame.draw.circle(screen, (149,160,163), (505,513),5)
        pygame.draw.circle(screen, (149,160,163), (450,575),5)
        pygame.draw.circle(screen, (149,160,163), (450,365),5)
        
        #Drawing Lines in body
        pygame.draw.line (screen, (149,160,163),(400,595),(400,570),3)
        pygame.draw.line (screen, (149,160,163),(400,370),(400,315),3)
        pygame.draw.line (screen, (149,160,163),(300,470),(275,470),3)
        pygame.draw.line (screen, (149,160,163),(500,470),(525,470),3)
        pygame.draw.line (screen, (149,160,163),(455, 385),(465, 375),3)
        pygame.draw.line (screen, (149,160,163),(465, 375),(495, 410),3)
        pygame.draw.line (screen, (149,160,163),(495, 410),(485,420),3)
        pygame.draw.line (screen, (255,255,255),(374, 507),(421,436),3)
        pygame.draw.line (screen, (255,255,255),(374, 522),(431,438),3)
        pygame.draw.line (screen, (255,255,255),(369, 502),(421,424),3)
           
        pygame.display.flip ()
        pygame.time.wait(100)
