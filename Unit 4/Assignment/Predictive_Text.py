# Name: Moustafa Eid
# Date: May 31 2017
# Class: ICS3U1-03
# Description: Lists Assignment - Predictive Text

# Importing all necessary sources
import pygame
import random

# Initiating pygame and Creating screen
pygame.init()
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

# Declaring variables for program
running = True  # Variable that makes program run
myClock = pygame.time.Clock()   # Program that creats fps
letter = "" #Variable that stores text
runmath = False
# Declaring All Fonts
fontinput = pygame.font.SysFont("Arial",28)
fontmenu = pygame.font.SysFont("Courier",50)
fontoutput = pygame.font.SysFont("Footlight MT Light",35)
fonterror = pygame.font.SysFont("Footlight MT Light",30)
# Loading up all images
titlePic = pygame.image.load("predictive.png")
titlePic = pygame.transform.scale(titlePic, (500,200))
namePic = pygame.image.load("name.png")
namePic = pygame.transform.scale(namePic, (250,100))

# Position for text
title = pygame.Rect (20,50,320,40)
title2 = pygame.Rect (220,180,320,40)
choice1 = pygame.Rect (30,280,320,40)
choice2 = pygame.Rect (300,280,320,40)
choice3 = pygame.Rect (600,280,320,40)

# Opening Text File
dictFile = open("dict.txt", "r")

# Declaring Lists
dictionary = []
words = []
repetition = []
sortednum = []
letterList = []
numberList = []
sortednumberList = []

# Declaring Accumulators and Counters
count = 0
loop = 0
pos = 0
run = 0
time = 0

# Function for Keyboard Input
def interface():
    global letter
    if evnt.key == pygame.K_BACKSPACE:
        letter = letter[0:-1]
    if evnt.key == pygame.K_SPACE:
        letter += " "
    if evnt.key == pygame.K_a:
        letter += "a"
    if evnt.key == pygame.K_b:
        letter += "b"
    if evnt.key == pygame.K_c:
        letter += "c"
    if evnt.key == pygame.K_d:
        letter += "d"
    if evnt.key == pygame.K_e:
        letter += "e"
    if evnt.key == pygame.K_f:
        letter += "f"
    if evnt.key == pygame.K_g:
        letter += "g"
    if evnt.key == pygame.K_h:
        letter += "h"
    if evnt.key == pygame.K_i:
        letter += "i" 
    if evnt.key == pygame.K_j:
        letter += "j"
    if evnt.key == pygame.K_k:
        letter += "k"
    if evnt.key == pygame.K_l:
        letter += "l"
    if evnt.key == pygame.K_m:
        letter += "m"
    if evnt.key == pygame.K_n:
        letter += "n"
    if evnt.key == pygame.K_o:
        letter += "o"
    if evnt.key == pygame.K_p:
        letter += "p"
    if evnt.key == pygame.K_q:
        letter += "q"
    if evnt.key == pygame.K_r:
        letter += "r"
    if evnt.key == pygame.K_s:
        letter += "s" 
    if evnt.key == pygame.K_t:
        letter += "t" 
    if evnt.key == pygame.K_u:
        letter += "u"  
    if evnt.key == pygame.K_v:
        letter += "v"
    if evnt.key == pygame.K_w:
        letter += "w"
    if evnt.key == pygame.K_x:
        letter += "x"
    if evnt.key == pygame.K_y:
        letter += "y"
    if evnt.key == pygame.K_z:
        letter += "z"
        
# Function that calculates the top 3 for every different combination of numbers
def math():
    global letter, letterList, numberList, sortednumberList, pos, run, loop, pos1, pos2, pos3, top1, top2, repeat1, repeat2, repeat3, repetition, prediction
    # appends words that start with input anf how many times they are repeated to lists
    for prediction in words:
        if prediction[0:len(letter)] == letter:
            letterList.append(prediction)
            numberList.append(repetition[loop])
            sortednumberList.append(repetition[loop])
        loop += 1
    sortednumberList.sort()
    
    # Stores top3 in to variables
    if len(letterList) >= 1:
        top1 = sortednumberList[len(sortednumberList)-1]
    if len(letterList) >= 2:
        top2 = sortednumberList[len(sortednumberList)-2]
    if len(letterList) >= 3:
        top3 = sortednumberList[len(sortednumberList)-3]  
    
    # If there is only 1 word in list
    if len(letterList) >= 1:
        for top in numberList:
            if top == top1:
                repeat1 = top
                pos1 = pos
                break
            pos += 1
        pos = 0
    
    # If there is 2 words in the list    
    if len(letterList) >= 2:
        # If none are equal
        if top1 != top2:
            for top in numberList:
                if top == top1:
                    repeat1 = top
                    pos1 = pos
                    break
                pos += 1
            pos = 0   
            for top in numberList:
                if top == top2:
                    if top != repeat1:
                        repeat2 = top
                        pos2 = pos
                        break
                pos += 1
            pos = 0
            run = 0
        # If all are equal
        elif top1 == top2:
            for top in numberList:
                if top == top1:
                    repeat1 = top
                    pos1 = pos
                    break
                pos += 1
            pos = 0   
            for top in numberList:
                if top == top2:
                    run += 1
                    if run == 2:
                        repeat2 = top
                        pos2 = pos
                        break
                pos += 1
            pos = 0
            run = 0 
    
    # If there is 3 words or more in the list
    if len(letterList) >= 3: 
        # if none are repeated the same times
        if top1 != top2 and top1 != top3 and top2 != top3:
            for top in numberList:
                if top == top1:
                    repeat1 = top
                    pos1 = pos
                    break
                pos += 1
            pos = 0
            
            for top in numberList:
                if top == top2:
                    if top != repeat1:
                        repeat2 = top
                        pos2 = pos
                        break
                pos += 1
            pos = 0
            run = 0
            
            for top in numberList:
                if top == top3:
                    if top != repeat2 and top != repeat1:        
                        repeat3 = top
                        pos3 = pos
                        break
                pos += 1
        # If all are repeated same times       
        elif top1 == top2 and top1 == top3:
            for top in numberList:
                if top == top1:
                    repeat1 = top
                    pos1 = pos
                    break
                pos += 1
            pos = 0 
            
            for top in numberList:
                if top == top2:
                    run += 1
                    if run == 2:
                        repeat2 = top
                        pos2 = pos
                        break
                pos += 1
            pos = 0
            run = 0
            
            for top in numberList:
                if top == top3:
                    run += 1
                    if run == 3:
                        repeat3 = top
                        pos3 = pos
                        break
                pos += 1
        # If first 2 are same but last isnt       
        elif top1 == top2 and top1 != top3:
            for top in numberList:
                if top == top1:
                    repeat1 = top
                    pos1 = pos
                    break
                pos += 1
            pos = 0   
            
            for top in numberList:
                if top == top2:
                    run += 1
                    if run == 2:
                        repeat2 = top
                        pos2 = pos
                        break
                pos += 1
            pos = 0
            run = 0
            
            for top in numberList:
                if top == top3:
                    if top != repeat2 and top != repeat1:        
                        repeat3 = top
                        pos3 = pos
                        break
                pos += 1
        # If 1st and last are same but middle is not        
        elif top1 != top2 and top1 == top3:
            for top in numberList:
                if top == top1:
                    repeat1 = top
                    pos1 = pos
                    break
                pos += 1
            pos = 0
            
            for top in numberList:
                if top == top2:
                    run += 1
                    if run == 2:
                        repeat2 = top
                        pos2 = pos
                        break
                pos += 1
            pos = 0
            run = 0
            
            for top in numberList:
                if top == top3:
                    if top != repeat2 and top != repeat1:        
                        repeat3 = top
                        pos3 = pos
                        break
                pos += 1
        # If last 2 are same but first is not        
        elif top1 != top2 and top1 != top3 and top2 == top3:
            for top in numberList:
                if top == top1:
                    repeat1 = top
                    pos1 = pos
                    break
                pos += 1
            pos = 0
            
            for top in numberList:
                if top == top2:
                    run += 1
                    if run == 2:
                        repeat2 = top
                        pos2 = pos
                        break
                pos += 1
            pos = 0
            run = 0
            
            for top in numberList:
                if top == top3:
                    repeat3 = top
                    pos3 = pos
                    break
                pos += 1    

# While loop that stores text file in to a list
while True:
    text = dictFile.readline()
    if text == "":
        break
    dictionary.append(text[:-1]) 
dictFile.close()

# Loop that appends a list without repeating words
for text in dictionary:
    if text not in words:
        words.append(text)

# Loop that calculates the number of times a word is repeated
for text in words:
    for nums in dictionary:
        if text == nums:
            count += 1
    repetition.append(count)
    sortednum.append(count)    
    count = 0
# Sorts the list for smallest to biggest
sortednum.sort()


        
    
            
            
# Fills Screen Blue
screen.fill(BLUE)    
#Main loop that checks events
while running:
    # Closes program when x is clicked
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
        # If keyboard is clicked
        if evnt.type == pygame.KEYDOWN:
            interface()
            runmath = True
            # Random coulours for output
            R = random.randint (125,255)
            G = random.randint (125,255)
            B = random.randint (0,255)
    # Draws Text Box
    pygame.draw.rect(screen, (WHITE), pygame.Rect(260,53,200,33))
    pygame.draw.rect(screen, (BLACK), pygame.Rect(260,53,200,33),2)    
    
    # Draws Text for input
    texttitle1 = fontinput.render("Please Type the Word:", 1, RED)
    screen.blit(texttitle1, title)
    texttitle1 = fontinput.render(letter, 1, BLACK)
    screen.blit(texttitle1, pygame.Rect(265,50,200,30))
    # Draws text with output after iput is entered
    if runmath == True:
        math()
        screen.fill(BLUE)
        if len(letterList) > 0:
            texttitle2 = fontmenu.render("Did you mean?", 1, GREEN)
            screen.blit(texttitle2, title2)
        # Error Handling
        if len(letterList) == 0:
            texterror = fonterror.render("Sorry the dictionary does not contain a word that starts with these letters", 1, BLACK)
            screen.blit(texterror, choice1)  
        # If only 1 word in list
        if len(letterList) >= 1:        
            textchoice1 = fontoutput.render("1. %s" % (letterList[pos1]), 1, (R,G,B))
            screen.blit(textchoice1, choice1)
            textchoice1 = fontoutput.render("Occurs: %i times." % (repeat1), 1, BLACK)
            screen.blit(textchoice1,pygame.Rect(30,320,320,40))  
        # If only 2 word in list        
        if len(letterList) >= 2:
            textchoice2 = fontoutput.render("2. %s" % (letterList[pos2]), 1, (R,G,B))
            screen.blit(textchoice2, choice2)
            textchoice2 = fontoutput.render("Occurs: %i times." % (repeat2), 1, BLACK)
            screen.blit(textchoice2,pygame.Rect(300,320,320,40))
        # If 3 or more words in list
        if len(letterList) >= 3:
            textchoice3 = fontoutput.render("3. %s" % (letterList[pos3]), 1, (R,G,B))
            screen.blit(textchoice3, choice3)
            textchoice3 = fontoutput.render("Occurs: %i times." % (repeat3), 1, BLACK)
            screen.blit(textchoice3,pygame.Rect(600,320,320,40))
        # Resets Everything after each letter
        runmath = False
        letterList = []
        numberList = []
        sortednumberList = []
        pos = 0
        run = 0
        loop = 0
    # Images rendering
    screen.blit(titlePic, pygame.Rect(20,400,50,78))                    
    screen.blit(namePic, pygame.Rect (530,500,50,78))                    
    pygame.display.flip()    
        
    # Flips everything
    pygame.display.flip()
    # 10000 FPS
    myClock.tick(1000)
    
# Quits program when done
pygame.quit()