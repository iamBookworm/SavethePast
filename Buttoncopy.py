import pygame
from pygame import *
import tkinter
from tkinter import *
import sys
import os
import time
import random
pygame.init()
fps= 40
ani = 4
clock= pygame.time.Clock()
#Different Colors
white = (255,255,255)
limegreen = (50, 205, 50)
lime = (0,255,0)
black = (0,0,0)
worldx=800
worldy=800
done = False
def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()
def Button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(world, ac, (x,y,w,h)) #Change color
        if click[0] == 1 and action != None:
            if action == "play":


                #CharacterSelect()
            #elif action == "quit":
                #pygame.quit()
                #quit()
    else:
        pygame.draw.rect(world, ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)) )
    world.blit(textSurf,textRect)
def CharacterSelect():
    world = pygame.display.set_mode([worldx,worldy])
    image = pygame.image.load('pixil-frame-1.png').convert()
    current_path = os.path.dirname('Final_Project')

    background_image = pygame.image.load(os.path.join(current_path, 'pixil-frame-1.png'))
    pygame.display.flip()
while not done:
    world = pygame.display.set_mode([worldx,worldy])
    image = pygame.image.load('pixil-frame-0.png').convert()
    current_path = os.path.dirname('Final_Project')

    background_image = pygame.image.load(os.path.join(current_path, 'pixil-frame-1.png'))

    # background_image = pygame.image.load(os.path.join(image_path)"pixil-frame-0.png").convert()
    world.blit(image,[0,0])
    Button("Start", 230,50,200,100, limegreen, lime, "play")
    pygame.display.update()
    pygame.display.flip()
