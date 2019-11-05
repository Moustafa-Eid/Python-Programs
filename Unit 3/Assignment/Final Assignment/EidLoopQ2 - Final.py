# Name: Moustafa Eid
# Date: May 8 2017
# Class: ICS3U1-03
# Description: Repetition Assignment - Menu screen that displays a computer virus and a computer crime

# Importing all necessary sources
import pygame
import time
import math
import random


# Initiating pygame and Creating screen
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048) # Eliminates sound lag from program
size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)

# Define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
GREY = (142,143,147)
BROWN = (170,83,1)
color = pygame.Color(0, 0, 255, 0)
background_color = pygame.Color(0, 0, 0, 0)

# Declaring variables for program
canimation = 1  # Controls criminal walking
run = 0     # eliminates music plaing in over each other
welcomex = 0    # Moves welcome sign
mousehistory = 0    # Takes history of mouse
menuopt = 0     # Menu option
canvas_width = 800      #For sine wave
canvas_height = 600     #For sine wave
running = True  # Variable that makes program run
myClock = pygame.time.Clock()   # Program that creats fps


# Declares fonts used in program
fontmenu = pygame.font.SysFont("French Script MT Regular",60)
fontvirus = pygame.font.SysFont("Arial",28)
fontback = pygame.font.SysFont("Times New Roman",50)
fontpolice = pygame.font.SysFont("Times New Roman",40)
fontwelcome = pygame.font.SysFont("Times New Roman",100)

# Declares Pictures in the program 
trojanPic = pygame.image.load("trojan.png")
phishingPic = pygame.image.load("phishing.png")
virusPic = pygame.image.load("virus.png")
virusPic = pygame.transform.scale(virusPic, (300,200))
flarePic = pygame.image.load("flare.png")
flare1Pic = pygame.image.load("flare1.png")
flare1Pic = pygame.transform.scale(flare1Pic, (400,300))

# Declares sounds used in the program
virusSound = pygame.mixer.Sound("dangers.wav")
policeSound = pygame.mixer.Sound("police.wav")
menuSound = pygame.mixer.Sound("menumusic.wav")

# Creates a rectangle for the indicator box
indicator = pygame.Rect(260,150,320,37)
indicator2 = pygame.Rect (260, 300, 333, 37)
indicator3 = pygame.Rect (360, 450, 87, 37)

# Position for Virus Text
virustitle = pygame.Rect (340,20,320,40)
virus1 = pygame.Rect (20,70,320,40)
virus2 = pygame.Rect (20,100,320,40)
virus3 = pygame.Rect (20,130,320,40)
virus4 = pygame.Rect (20,160,320,40)
virus5 = pygame.Rect (20,190,320,40)
virus6 = pygame.Rect (20,220,320,40)
virus7 = pygame.Rect (20,250,320,40)
virus8 = pygame.Rect (20,280,320,40)
virus9 = pygame.Rect (20,310,320,40)
virus10 = pygame.Rect (20,340,320,40)
virus11 = pygame.Rect (20,370,320,40)
virus12 = pygame.Rect (20,400,320,40)
virus13 = pygame.Rect (20,430,320,40)
virus14 = pygame.Rect (20,460,320,40)
virus15 = pygame.Rect (20,490,320,40)

# Position for police text
police = pygame.Rect(330,230,400,50)

# Position for welcome text
welcome = pygame.Rect(welcomex,300,100,100)

# Position for crime text
crime = pygame.Rect (250,300,320,40)

# Position for back button
back = pygame.Rect (5,540,103,47)

# Defining function for virus text
def textvirus():
    textvirustitle = fontback.render("Trojans!" , 1, RED)
    screen.blit(textvirustitle, virustitle)
    textvirus1 = fontvirus.render("A Trojan virus is a virus that is sent to your computer via a hidden program. " , 1, BLACK)
    screen.blit(textvirus1, virus1)
    textvirus2 = fontvirus.render("A Trojan disguises itself as an important program to make you believe it's " , 1, BLACK)
    screen.blit(textvirus2, virus2)
    textvirus3 = fontvirus.render("safe. A Trojan virus usually plants itseld in highly desireable downloads " , 1, BLACK)
    screen.blit(textvirus3, virus3)
    textvirus4 = fontvirus.render("such as Games, Movies, Music and any Freeware. Trojans do not multiply" , 1, BLACK)
    screen.blit(textvirus4, virus4)
    textvirus5 = fontvirus.render("or spread like other viruses. However they are very dangerous because" , 1, BLACK)
    screen.blit(textvirus5, virus5)
    textvirus6 = fontvirus.render("they can record your login input and send it to hackers worldwide." , 1, BLACK)
    screen.blit(textvirus6, virus6)
    textvirus7 = fontvirus.render("Trojan Viruses are highly used among cyber thieves to steal your" , 1, BLACK)
    screen.blit(textvirus7, virus7)
    textvirus8 = fontvirus.render("financial information and personal data. To avoid trojans do not" , 1, BLACK)
    screen.blit(textvirus8, virus8)
    textvirus9 = fontvirus.render("download any files from untrusted sources and websites." , 1, BLACK)
    screen.blit(textvirus9, virus9)
    textvirus10 = fontvirus.render("An Example of a Trojan virus is ZeuS:" , 1, BLACK)
    screen.blit(textvirus10, virus10)
    textvirus11 = fontvirus.render("It is estimated to have affected 3.6 million PC's in the US in 2009" , 1, BLACK)
    screen.blit(textvirus11, virus11)
    textvirus12 = fontvirus.render("The virus had stolen over $70 million in 1 year" , 1, BLACK)
    screen.blit(textvirus12, virus12)
    textvirus13 = fontvirus.render("More than 100 people were arrested on charges of conspiracy to commit" , 1, BLACK)
    screen.blit(textvirus13, virus13)
    textvirus14 = fontvirus.render("bank fraud and money laundering, over 90 in the US, and the others in" , 1, BLACK)
    screen.blit(textvirus14, virus14)
    textvirus15 = fontvirus.render("the UK and Ukraine" , 1, BLACK)
    screen.blit(textvirus15, virus15)
 
# Defining funvtion for Crime text  
def textcrime():
    textcrimetitle = fontback.render("Phishing!" , 1, RED)
    screen.blit(textcrimetitle, virustitle)
    textcrime1 = fontvirus.render("Phishing is the act of sending an email to a user falsely claiming to be" , 1, GREEN)
    screen.blit(textcrime1, virus1)     
    textcrime2 = fontvirus.render("an established legitimate enterprise in an attempt to scam the user into" , 1, GREEN)
    screen.blit(textcrime2, virus2)
    textcrime3 = fontvirus.render("surrendering private information that will be used for identity theft." , 1, GREEN)
    screen.blit(textcrime3, virus3)
    textcrime4 = fontvirus.render("Phishing email will typically direct the user to visit a website where" , 1, GREEN)
    screen.blit(textcrime4, virus4)
    textcrime5 = fontvirus.render("they are asked to update personal information, such as a password, " , 1, GREEN)
    screen.blit(textcrime5, virus5)    
    textcrime6 = fontvirus.render("credit card, social security, or bank account numbers, that the" , 1, GREEN)
    screen.blit(textcrime6, virus6)
    textcrime7 = fontvirus.render("legitimate organization already has. The website, however, is fake" , 1, GREEN)
    screen.blit(textcrime7, virus7)
    textcrime8 = fontvirus.render("and will capture and steal any information the user enters on the page" , 1, GREEN)
    screen.blit(textcrime8, virus8)     

# Defining function for menu 
def menu():
    global mousehistory, mb, mx, my, menuopt, running, run  # making all variables global
    # Starts program and plays music
    if mousehistory == 0:
        if run == 0 and mousehistory == 0:
            menuSound.play()
            run = 1
        # Draws the 3 options in menu
        screen.blit(virusPic, pygame.Rect(500,400,50,78))                    
        text1 = fontmenu.render("Computer Virus" , 1, GREEN)
        screen.blit(text1, indicator)
        text2 = fontmenu.render("Computer Crime" , 1, GREEN)
        screen.blit(text2, indicator2)        
        text3 = fontmenu.render("Quit" , 1, GREEN)
        screen.blit(text3, indicator3)
        # Makes a mouse over effect on first option and tells it what to do when mouse is clicked
        if indicator.collidepoint(mx,my) and mousehistory == 0:
            if mb == 0:
                text1 = fontmenu.render("Computer Virus" , 1, RED)
                screen.blit(text1, indicator)
            if mb == 1:
                mousehistory = 1
                menuopt = 1
                # Stops menu music
                pygame.mixer.stop()            
                run = 0
        # Makes a mouse over effect on second option and tells it what to do when mouse is clicked
        if indicator2.collidepoint(mx,my) and mousehistory == 0:
            if mb == 0:            
                text2 = fontmenu.render("Computer Crime" , 1, RED)
                screen.blit(text2, indicator2)
            if mb == 1:              
                mousehistory = 1
                menuopt = 2
                # Stops menu music
                pygame.mixer.stop()                            
                run = 0
                
        # Makes a mouse over effect on third option and tells it what to do when mouse is clicked        
        if indicator3.collidepoint(mx,my) and mousehistory == 0:
            if mb == 0:
                text3 = fontmenu.render("Quit" , 1, RED)
                screen.blit(text3, indicator3)
            if mb == 1:
                mousehistory = 1
                menuopt = 3
                # Stops menu music
                pygame.mixer.stop()            
                run = 0
    # If Mouse is clicked the following happens
    if mousehistory == 1:
        if menuopt == 1 and mousehistory == 1:
            if run == 0:
                # Plays danger noise
                virusSound.play()
                # Draws skulls
                for skull in range (100):
                    skullx = random.randint(0,800)
                    skully = random.randint(0,600)                    
                    virusanimation(skullx,skully)
                    pygame.time.wait(10)
                    pygame.display.update()
            # Filling background blue and calls virus text function
            screen.fill(BLUE)
            screen.blit(trojanPic, pygame.Rect(250,100,50,78))
            textvirus()
            textback = fontback.render("Back" , 1, GREEN)
            screen.blit(textback, back)
            run += 1         
            # Mouse over effect on back button and goes back to menu when clicked
            if back.collidepoint(mx,my):                 
                if mb == 0:
                    textback = fontback.render("Back" , 1, RED)
                    screen.blit(textback, back)
                if mb == 1:
                    screen.fill (WHITE)
                    mousehistory = 0
                    run = 0
                    # Stops sounds
                    pygame.mixer.stop()
        # Menu option 2 content
        if menuopt == 2 and mousehistory == 1:
            if run == 0:
                # Police siren plays and police picture appears
                policeSound.play()
                screen.fill(BLACK)
                policesiren()
                screen.blit(flarePic, pygame.Rect(20,80,105,78))
                screen.blit(flare1Pic, pygame.Rect(450,100,105,78))                                                                
                pygame.display.flip()
                pygame.time.wait(3000)
                # Criminal runs animation
                for cmove in range(1,900,40):
                    global canimation
                    screen.fill(BLACK)
                    if canimation == 1:
                        criminal1(cmove)
                        legs1(cmove)
                        canimation = 2
                    elif canimation == 2:
                        criminal2(cmove)
                        legs2(cmove)
                        canimation = 1
    
                    pygame.time.wait(200)
             
            # Fills screen blue and and calls crime text function   
            screen.fill(BLUE)
            screen.blit(phishingPic, pygame.Rect(0,20,50,78))                        
            textcrime()
            textback = fontback.render("Back" , 1, GREEN)
            screen.blit(textback, back)
            run += 1
            # Mouse over effect on back button and goes back to menu when clicked
            if back.collidepoint(mx,my):                 
                if mb == 0:
                    textback = fontback.render("Back" , 1, RED)
                    screen.blit(textback, back)
                if mb == 1:
                    screen.fill (WHITE)
                    mousehistory = 0  
                    run = 0
                    # Stops police sounds
                    pygame.mixer.stop()
        # Quits program when option 3 is selected
        if menuopt == 3 and mousehistory == 1:
            running = False

# Function that creates sine graphs in menu
def sine():
    frequency = 4
    amplitude = 50 # in px
    speed = 1
    for x in range(0, canvas_width):
        y = int((canvas_height/4) + amplitude*math.sin(frequency*((float(x)/canvas_width)*(2*math.pi) + (speed*time.time()))))
        screen.set_at((x, y), color)
    screen.blit(screen, (0, 0))
    for x in range(0, canvas_width):
        y = int((canvas_height/2) + amplitude*math.sin(frequency*((float(x)/canvas_width)*(2*math.pi) + (speed*time.time()))))
        screen.set_at((x, y), color)
    screen.blit(screen, (0, 0))
    for x in range(0, canvas_width):
        y = int((450) + amplitude*math.sin(frequency*((float(x)/canvas_width)*(2*math.pi) + (speed*time.time()))))
        screen.set_at((x, y), color)
    screen.blit(screen, (0, 0))

# Function that creates skulls when virus is clicked 
def virusanimation(x,y):
    pygame.draw.line(screen,(255,255,255), (x,y) , (x+102,y+153),10)
    pygame.draw.line(screen,(255,255,255), (x+22,y+153) , (x+124,y),10)
    pygame.draw.ellipse(screen, (255,255,255), pygame.Rect(x+12,y+10,100,133))
    pygame.draw.polygon(screen, (255,255,255), [[x+17, y+60], [x+52, y+150],[x+72, y+52],[x+107,y+60]])
    pygame.draw.ellipse(screen, (0,0,0), pygame.Rect(x+32,y+85,60,40),1)
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(x+32,y+65,60,40))
    pygame.draw.line(screen,(0,0,0), (x+32,y+105), (x+92,y+105),1)
    pygame.draw.line(screen,(0,0,0), (x+42,y+105) , (x+42,y+117),1)
    pygame.draw.line(screen,(0,0,0), (x+52,y+105) , (x+52,y+121),1)
    pygame.draw.line(screen,(0,0,0), (x+62,y+105) , (x+62,y+123),1)
    pygame.draw.line(screen,(0,0,0), (x+72,y+105) , (x+72,y+121),1)
    pygame.draw.line(screen,(0,0,0), (x+82,y+105) , (x+82,y+117),1)
    pygame.draw.circle(screen,(0,0,0),(x+42,y+50),15)
    pygame.draw.circle(screen,(0,0,0),(x+82,y+50),15)
    pygame.draw.polygon(screen, (0,0,0), [[x+57, y+70], [x+62, y+60],[x+67, y+70]])
    pygame.draw.line(screen,(255,255,255), (x+62,y+70) , (x+62,y+60),1)
    pygame.display.flip()

# Function that draws police siren when crime is clicked    
def policesiren():
    pygame.draw.rect(screen, (6,61,162), pygame.Rect(100,200,190,100))
    pygame.draw.polygon(screen, (6,61,162), [[100, 200], [120, 170],[310,170],[290,200]])
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(290,200,210,100))
    pygame.draw.polygon(screen, (255,255,255), [[290, 200], [310, 170],[520,170],[500,200]])
    pygame.draw.rect(screen, (253,3,8), pygame.Rect(500,200,190,100))
    pygame.draw.polygon(screen, (253,3,8), [[500, 200], [520, 170],[710,170],[690,200]])
    pygame.draw.polygon(screen, (253,3,8), [[690, 200], [710, 170],[710,270],[690,300]])
    pygame.draw.line (screen, (116,103,107),(100, 300),(690, 300),5)
    pygame.draw.line (screen, (116,103,107),(690, 300),(710, 270),2)
    pygame.draw.line (screen, (116,103,107),(690, 300),(690, 200),2)
    pygame.draw.line (screen, (116,103,107),(690, 200),(710, 170),2)
    pygame.draw.line (screen, (116,103,107),(690, 200),(100, 200),2)
    pygame.draw.line (screen, (116,103,107),(100, 300),(100, 200),2)
    pygame.draw.line (screen, (116,103,107),(100, 200),(120, 170),2)
    pygame.draw.line (screen, (116,103,107),(290, 200),(310, 170),2)
    pygame.draw.line (screen, (116,103,107),(500, 200),(520, 170),2)
    pygame.draw.line (screen, (116,103,107),(120, 170),(710, 170),2)
    pygame.draw.line (screen, (116,103,107),(290, 300),(290, 200),2)
    pygame.draw.line (screen, (116,103,107),(500, 300),(500, 200),2)
    textpolice = fontpolice.render("POLICE" , 1, BLACK)
    screen.blit(textpolice, police) 
    pygame.display.flip()
    
# Function that draws criminal in animation 1
def criminal1(cmove):
    pygame.draw.polygon(screen, (WHITE), [[cmove, 225], [cmove+20, 225],[cmove+25, 325],[cmove-5,325]])
    pygame.draw.circle(screen, (255,218,185), (cmove+10,200),30)
    pygame.draw.rect(screen, (BLACK), pygame.Rect(cmove+15,190,40,10))
    pygame.draw.circle(screen, (WHITE), (cmove+25,197),2)
    pygame.draw.rect(screen, (BLACK), pygame.Rect(cmove-25,165,45,15))
    pygame.draw.rect(screen, (BLACK), pygame.Rect(cmove-25,165,45,15))
    pygame.draw.rect(screen, (BLACK), pygame.Rect(cmove-25,165,25,17))
    pygame.draw.line(screen,BLACK, (cmove+25,210) , (cmove+42,210),2)
    pygame.draw.line(screen,BROWN, (cmove+25,205) , (cmove+40,205),4)
    pygame.draw.line(screen,BLACK, (cmove-2,240) , (cmove+22,240),10)
    pygame.draw.line(screen,BLACK, (cmove-2,255) , (cmove+22,255),10)
    pygame.draw.line(screen,BLACK, (cmove-2,270) , (cmove+22,270),10)
    pygame.draw.line(screen,BLACK, (cmove-4,285) , (cmove+24,285),10)
    pygame.draw.line(screen,BLACK, (cmove-4,300) , (cmove+24,300),10)
    pygame.draw.line(screen,BLACK, (cmove-4,315) , (cmove+24,315),10)
    pygame.display.flip()
    
# Function that draws criminal in animation 2
def criminal2(cmove):
    pygame.draw.polygon(screen, (WHITE), [[cmove, 225], [cmove+20, 225],[cmove+25, 325],[cmove-5,325]])
    pygame.draw.circle(screen, (255,218,185), (cmove+10,200),30)
    pygame.draw.rect(screen, (BLACK), pygame.Rect(cmove+15,190,40,10))
    pygame.draw.circle(screen, (WHITE), (cmove+25,197),2)
    pygame.draw.rect(screen, (BLACK), pygame.Rect(cmove-25,165,45,15))
    pygame.draw.rect(screen, (BLACK), pygame.Rect(cmove-25,165,45,15))
    pygame.draw.rect(screen, (BLACK), pygame.Rect(cmove-25,165,25,17))
    pygame.draw.line(screen,BLACK, (cmove+25,210) , (cmove+42,210),2)
    pygame.draw.line(screen,BROWN, (cmove+25,205) , (cmove+40,205),4)
    pygame.draw.line(screen,BLACK, (cmove-2,240) , (cmove+22,240),10)
    pygame.draw.line(screen,BLACK, (cmove-2,255) , (cmove+22,255),10)
    pygame.draw.line(screen,BLACK, (cmove-2,270) , (cmove+22,270),10)
    pygame.draw.line(screen,BLACK, (cmove-4,285) , (cmove+24,285),10)
    pygame.draw.line(screen,BLACK, (cmove-4,300) , (cmove+24,300),10)
    pygame.draw.line(screen,BLACK, (cmove-4,315) , (cmove+24,315),10)
    pygame.display.flip()

# Function that draws legs in animation 1
def legs1(cmove):
    pygame.draw.polygon(screen, (86,115,104), [[cmove, 325], [cmove-10, 340],[cmove-80, 325],[cmove-85,330],[cmove-5,360],[cmove+15,330],[cmove+15,325]])
    pygame.draw.polygon(screen, (GREY), [[cmove+15,325],[cmove+15,330],[cmove+30, 340],[cmove+30,400],[cmove+45,400],[cmove+40,327],[cmove-5,325]])
    pygame.draw.polygon(screen, (RED), [[cmove-80,325],[cmove-85,320],[cmove-90, 340],[cmove-85,345]])
    pygame.draw.rect(screen, (RED), pygame.Rect(cmove+30,400,25,7))    
    pygame.display.flip()
    
    
# Function that draws legs in animation 2
def legs2(cmove):
    pygame.draw.polygon(screen, (86,115,104), [[cmove+10, 325], [cmove+70, 370],[cmove+80, 400],[cmove+65,400],[cmove+55,370],[cmove,325]])    
    pygame.draw.polygon(screen, (GREY), [[cmove+15,325],[cmove-30,380],[cmove-50, 325],[cmove-40,315],[cmove-25,360],[cmove,325]])
    pygame.draw.polygon(screen, (RED), [[cmove-40,315],[cmove-45,310],[cmove-70, 330],[cmove-65,335]])
    pygame.draw.rect(screen, (RED), pygame.Rect(cmove+65,400,25,7))    
    pygame.display.flip()
    
    
                
#Getting mouse cordinates 
def getmouse():
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()[0]
    return (mx, my, mb)

# Loop that moves welcome text from left to right
for move in range (1,200):
        screen.fill(GREEN)
        textwelcome = fontwelcome.render("Welcome" , 1, BLUE)
        screen.blit(textwelcome, pygame.Rect(move,300,100,100))
        textwelcome = fontvirus.render("Program By: Moustafa Eid" , 1, RED)
        screen.blit(textwelcome, pygame.Rect(800-(move+100),500,100,100))        
        pygame.display.flip()
        pygame.time.wait(1)
pygame.time.wait(3000)

#Main loop that checks events
while running:
    # Closes program when x is clicked
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
    # Gets position of mouse and if mouse is clicked or not
    mx, my, mb = getmouse()
    # Fills background black
    screen.fill (BLACK)
    # calls sine function in background
    sine()
    # Calls menu function
    menu()
    # Flips everything
    pygame.display.flip()
    # 10000 FPS
    myClock.tick(1000)
    
# Quits program when done
pygame.quit()