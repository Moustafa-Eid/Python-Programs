# Name: Moustafa Eid
# Date: May 8 2017
# Class: ICS3U1-03
# Description: Repetition Assignment - Menu screen that displays a computer virus and a computer crime

# Importing all necessary sources
import pygame
import math
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
letter = ""
runmath = False
fontvirus = pygame.font.SysFont("Arial",28)
virus5 = pygame.Rect (300,190,320,40)
virus7 = pygame.Rect (300,230,320,40)
virus8 = pygame.Rect (30,280,320,40)
virus9 = pygame.Rect (300,280,320,40)
virus10 = pygame.Rect (600,280,320,40)

dictFile = open("dict.txt", "r")
dictionary = []
words = []
repetition = []
sortednum = []
letterList = []
numberList = []
sortednumberList = []
count = 0
loop = 0
pos = 0
run = 0
time = 0
start = 0

#Getting mouse cordinates 
def getmouse():
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()[0]
    return (mx, my, mb)
def interface():
    global letter
    if evnt.key == pygame.K_BACKSPACE:
        letter = letter[0:-1]
        math()
        output()
    if evnt.key == pygame.K_SPACE:
        letter += " "
        math()
        output()        
    if evnt.key == pygame.K_a:
        letter += "a"
        math()
        output()        
    if evnt.key == pygame.K_b:
        letter += "b"
        math()
        output()        
    if evnt.key == pygame.K_c:
        letter += "c"
        math()
        output()        
    if evnt.key == pygame.K_d:
        letter += "d"
        math()
        output()        
    if evnt.key == pygame.K_e:
        letter += "e"
        math()
        output()        
    if evnt.key == pygame.K_f:
        letter += "f"
        math()
        output()        
    if evnt.key == pygame.K_g:
        letter += "g"
        math()
        output()        
    if evnt.key == pygame.K_h:
        letter += "h"
        math()
        output()        
    if evnt.key == pygame.K_i:
        letter += "i" 
        math()
        output()        
    if evnt.key == pygame.K_j:
        letter += "j"
        math()
        output()        
    if evnt.key == pygame.K_k:
        letter += "k"
        math()
        output()        
    if evnt.key == pygame.K_l:
        letter += "l"
        math()
        output()        
    if evnt.key == pygame.K_m:
        letter += "m"
        math()
        output()        
    if evnt.key == pygame.K_n:
        letter += "n"
        math()
        output()        
    if evnt.key == pygame.K_o:
        letter += "o"
        math()
        output()        
    if evnt.key == pygame.K_p:
        letter += "p"
        math()
        output()        
    if evnt.key == pygame.K_q:
        letter += "q"
        math()
        output()        
    if evnt.key == pygame.K_r:
        letter += "r"
        math()
        output()        
    if evnt.key == pygame.K_s:
        letter += "s" 
        math()
        output()        
    if evnt.key == pygame.K_t:
        letter += "t" 
        math()
        output()        
    if evnt.key == pygame.K_u:
        letter += "u" 
        math()
        output()        
    if evnt.key == pygame.K_v:
        letter += "v"
        math()
        output()        
    if evnt.key == pygame.K_w:
        letter += "w"
        math()
        output()        
    if evnt.key == pygame.K_x:
        letter += "x"
        math()
        output()        
    if evnt.key == pygame.K_y:
        letter += "y"
        math()
        output()        
    if evnt.key == pygame.K_z:
        letter += "z"
        math()
        output()        
def math():
    global letter, letterList, numberList, sortednumberList, pos, run, loop, pos1, pos2, pos3, top1, top2, repeat1, repeat2, repeat3, repetition, prediction
    for prediction in words:
        if prediction[0:len(letter)] == letter:
            letterList.append(prediction)
            numberList.append(repetition[loop])
            sortednumberList.append(repetition[loop])
        loop += 1
    sortednumberList.sort()
    if len(letterList) >= 1:
        top1 = sortednumberList[len(sortednumberList)-1]
    if len(letterList) >= 2:
        top2 = sortednumberList[len(sortednumberList)-2]
    if len(letterList) >= 3:
        top3 = sortednumberList[len(sortednumberList)-3]        
    if len(letterList) >= 1:
        for top in numberList:
            if top == top1:
                repeat1 = top
                pos1 = pos
                break
            pos += 1
        pos = 0    
    if len(letterList) >= 2:
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
    if len(letterList) >= 3: 
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
                    #run += 1
                    #if run == 3:
                    repeat3 = top
                    pos3 = pos
                    break
                pos += 1
def output():
    global repeat1, letterList, ps1,pos2,pos3,repeat2,repeat3
    screen.fill(BLUE)
    if len(letterList) > 0:
        textvirus7 = fontvirus.render("Did you mean?", 1, BLACK)
        screen.blit(textvirus7, virus7)            
    if len(letterList) == 0:
        textvirus8 = fontvirus.render("Sorry the dictionary does not contain a word that starts with these letters", 1, BLACK)
        screen.blit(textvirus8, virus8)        
    if len(letterList) >= 1:        
        textvirus8 = fontvirus.render("1. %s." % (letterList[pos1]), 1, BLACK)
        screen.blit(textvirus8, virus8)
        textvirus8 = fontvirus.render("Occurs: %i times." % (repeat1), 1, BLACK)
        screen.blit(textvirus8,pygame.Rect(30,320,320,40))            
        pygame.display.flip()                    
    if len(letterList) >= 2:
        textvirus9 = fontvirus.render("2. %s" % (letterList[pos2]), 1, BLACK)
        screen.blit(textvirus9, virus9)
        textvirus9 = fontvirus.render("Occurs: %i times." % (repeat2), 1, BLACK)
        screen.blit(textvirus9,pygame.Rect(300,320,320,40))            
        pygame.display.flip()                    
    if len(letterList) >= 3:
        textvirus10 = fontvirus.render("3. %s" % (letterList[pos3]), 1, BLACK)
        screen.blit(textvirus10, virus10)
        textvirus10 = fontvirus.render("Occurs: %i times." % (repeat3), 1, BLACK)
        screen.blit(textvirus10,pygame.Rect(600,320,320,40))            
        pygame.display.flip()
        letterList = []
        numberList = []
        sortednumberList = []
        pos = 0
        run = 0
        loop = 0    
while True:
    text = dictFile.readline()
    if text == "":
        break
    dictionary.append(text[:-1]) 
dictFile.close()

for text in dictionary:
    if text not in words:
        words.append(text)

for text in words:
    for nums in dictionary:
        if text == nums:
            count += 1
    repetition.append(count)
    sortednum.append(count)    
    count = 0
sortednum.sort()


        
    
            
            

screen.fill(BLUE)    
#Main loop that checks events
while running:
    # Closes program when x is clicked
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
        if evnt.type == pygame.KEYDOWN:
            interface()
                               
                    
    # Gets position of mouse and if mouse is clicked or not
    mx, my, mb = getmouse()
    textvirus5 = fontvirus.render("Please Type the Word:", 1, BLACK)
    screen.blit(textvirus5, virus5)
    textvirus5 = fontvirus.render(letter, 1, BLACK)
    screen.blit(textvirus5, pygame.Rect (330,230,320,40))    
        

        
    # Flips everything
    pygame.display.flip()
    # 10000 FPS
    myClock.tick(1000)
    
# Quits program when done
pygame.quit()