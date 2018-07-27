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
def game_intro():
    # text_go, text_go_rect = text_objects("Start", smallText)
    # text_go_rect.center = ((230+(200/2)),(50+(100/2)))
    running = True
    while running:
        for event in pygame.event.get():
              print(event)
              if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Button("Start", 230,50,200,100, limegreen, lime, "play")
        pygame.display.flip()
        clock.tick(15)
    world.fill(white)
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
             pygame.time.wait(100)
             #world.fill(white)
             pygame.display.flip()
             image = pygame.image.load('tree.png').convert()
             world.blit(image,[0,0])
             pygame.display.flip()
            #if action == "play":
                #world.fill(white)

    else:
        pygame.draw.rect(world, ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)) )
    world.blit(textSurf,textRect)
def game_running():
    running = True

    while running:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


world = pygame.display.set_mode([worldx,worldy])
pygame.display.set_caption("Pollution")
largeText = pygame.font.Font('freesansbold.ttf',115)
smallText = pygame.font.Font("freesansbold.ttf",20)
image = pygame.image.load('openingscreen.png').convert()
current_path = os.path.dirname('SavethePast')
background_image = pygame.image.load(os.path.join(current_path, 'openingscreen.png'))

world.blit(image,[0,0])
clock = pygame.time.Clock()

game_intro()
# while not done:
#     world = pygame.display.set_mode([worldx,worldy])
#     image = pygame.image.load('pixil-frame-0.png').convert()
#     current_path = os.path.dirname('Final_Project')
#
#     background_image = pygame.image.load(os.path.join(current_path, 'pixil-frame-1.png'))
#
#     # background_image = pygame.image.load(os.path.join(image_path)"pixil-frame-0.png").convert()
#     world.blit(image,[0,0])
#     Button("Start", 230,50,200,100, limegreen, lime, "play")
#     pygame.display.update()
#     pygame.display.flip()
