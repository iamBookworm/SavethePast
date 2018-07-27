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
white = (255,255,255, 255)
limegreen = (50, 205, 50, 255)
lime = (0,255,0)
black = (0,0,0)
worldx=800
worldy=800
done = False

world = pygame.display.set_mode([worldx,worldy])
pygame.display.set_caption("Pollution")
background = pygame.Surface(world.get_size())
background = background.convert()
background.fill((250, 250, 250))
world.blit(background, [0,0])

largeText = pygame.font.Font('freesansbold.ttf',115)
smallText = pygame.font.Font("freesansbold.ttf",20)

image = pygame.image.load('openingscreen.png').convert()
current_path = os.path.dirname('Final_Project')

background_image = pygame.image.load(os.path.join(current_path, 'openingscreen.png'))
world.blit(image,[0,0])
clock = pygame.time.Clock()

def game_intro():
    running = True
    while running:
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Button("play")
        pygame.display.flip()
        clock.tick(15)

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def Button(action=None):
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and action != None:
        pygame.display.update()
        pygame.time.wait(100)
        pygame.display.flip()
        image = pygame.image.load('tree.png').convert()
        world.blit(image,[0,0])
        pygame.display.flip()

def game_running():
    running = True

    while running:

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

game_intro()
