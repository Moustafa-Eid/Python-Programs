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

# Draws the setting and scenery
pygame.draw.rect(screen, (244,205,162), pygame.Rect(0,300,800,500))
pygame.draw.rect(screen, (0, 74, 193), pygame.Rect(0,0,800,75))
pygame.draw.rect(screen, (15, 84, 196), pygame.Rect(0,75,800,65))
pygame.draw.rect(screen, (31, 95, 198), pygame.Rect(0,140,800,55))
pygame.draw.rect(screen, (56, 107, 188), pygame.Rect(0,195,800,45))
pygame.draw.rect(screen, (84, 125, 188), pygame.Rect(0,240,800,35))
pygame.draw.rect(screen, (110, 136, 178), pygame.Rect(0,275,800,25))
pygame.display.flip ()

#Drawing Head And Body Outline
pygame.draw.circle (screen, (255,255,255), (400,300), 100)
pygame.draw.rect(screen, (244,205,162), pygame.Rect(0,300,800,550))
pygame.draw.circle(screen, (0,0,0), (400,470),171,1)
pygame.draw.circle(screen, (255,255,255), (400,470),170)

#Drawing Head Features
#eyes
pygame.draw.circle(screen, (244,139,42), (400,655),60)
pygame.draw.circle(screen, (255,255,255), (400,650),40)

#neck
pygame.draw.polygon(screen, (255,255,255), [[300, 300], [350, 313],[450, 313],[500,300]])
pygame.draw.polygon(screen, (0,0,0), [[300, 300], [350, 313],[450, 313],[500,300]],1)

#drawing Outer Outlines
pygame.draw.line(screen,(115,121,126), (300,296) , (500,296),7)
pygame.draw.line(screen,(0,0,0), (300,292) , (500,292),1)

#sensor
pygame.draw.circle(screen,(0,0,0),(400,277),8,1)
pygame.draw.circle(screen,(0,0,0),(400,277),6,1)
pygame.draw.circle(screen,(0,0,0),(400,240),20)
pygame.draw.circle(screen,(65,70,74),(400,240),25,5)
pygame.draw.circle(screen,(0,0,0),(450,265),10)
pygame.draw.circle(screen,(65,70,74),(450,265),11,3)
pygame.draw.circle(screen,(65,70,74),(450,265),15,2)

#Drawing Head Colours and lines
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
pygame.display.flip ()

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

#sun

pygame.draw.circle(screen, (252, 212, 64), (200,100),70)
pygame.draw.circle(screen, (252, 212, 64), (70,200),30)

#clouds
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
pygame.display.flip ()

# Tie-Fighter

pygame.draw.polygon(screen, (183,187,193), [[520, 270], [510, 250],[520, 230],[540,235],[550,255],[540,275]])

pygame.draw.polygon(screen, (0,0,0), [[522, 268], [512, 250],[522, 232],[538,237],[548,255],[538,273]])


pygame.draw.circle(screen, (183,187,193), (531,255),5)

pygame.draw.line (screen, (183,187,193),(531, 255),(522,268),3)
pygame.draw.line (screen, (183,187,193),(531, 255),(512,250),3)
pygame.draw.line (screen, (183,187,193),(531, 255),(522,232),3)
pygame.draw.line (screen, (183,187,193),(531, 255),(538,237),3)
pygame.draw.line (screen, (183,187,193),(531, 255),(548,255),3)
pygame.draw.line (screen, (183,187,193),(531, 255),(538,273),3)

pygame.draw.polygon(screen, (73,75,77), [[529, 255], [530, 253],[550, 247],[550,256]])

pygame.draw.circle(screen, (142,143,147), (552,255),10)
pygame.draw.circle(screen, (0,0,0), (549,255),5)
pygame.draw.circle(screen, (142,143,147), (549,255),2,2)


pygame.draw.polygon(screen, (73,75,77), [[560, 247], [566, 250],[566, 253],[562,256]])

pygame.draw.polygon(screen, (183,187,193), [[572, 270], [562, 250],[572, 230],[592,235],[602,255],[592,275]])

pygame.draw.polygon(screen, (0,0,0), [[574, 268], [564, 250],[574, 232],[590,237],[600,255],[590,273]])

pygame.draw.circle(screen, (183,187,193), (585,255),5)

pygame.draw.line (screen, (183,187,193),(585, 255),(574,268),3)
pygame.draw.line (screen, (183,187,193),(585, 255),(564,250),3)
pygame.draw.line (screen, (183,187,193),(585, 255),(574,232),3)
pygame.draw.line (screen, (183,187,193),(585, 255),(590,237),3)
pygame.draw.line (screen, (183,187,193),(585, 255),(600,255),3)
pygame.draw.line (screen, (183,187,193),(585, 255),(590,273),3)

pygame.display.flip ()

# A Wing

pygame.draw.polygon(screen, (243,88,87), [[700, 150], [710, 160],[760, 100],[740,90]])
pygame.draw.polygon(screen, (234,220,197), [[710, 160],[750, 150],[760,145],[765,140],[748,110]])
pygame.draw.polygon(screen, (234,220,197), [[700, 150],[720, 100],[730,80],[735,90],[740,95]])

pygame.draw.polygon(screen, (234,220,197), [[748,110],[755,115],[760,100]])
pygame.draw.polygon(screen, (0,0,0), [[748,110],[755,115],[760,100]],1)

pygame.draw.polygon(screen, (234,220,197), [[730,95],[737,100],[742,85]])
pygame.draw.polygon(screen, (0,0,0), [[730,95],[737,100],[742,85]],1)



pygame.draw.line (screen, (31, 95, 198),(705, 155),(710,150),2)

pygame.draw.line (screen, (254,245,232),(690, 170),(689,172),2)
pygame.draw.line (screen, (254,245,232),(690, 180),(689,182),2)
pygame.draw.line (screen, (254,245,232),(680, 170),(679,172),2)

pygame.draw.circle (screen,(0,0,0),(730,124),5)
pygame.draw.circle (screen,(255,255,255),(730,124),1)


pygame.display.flip ()

