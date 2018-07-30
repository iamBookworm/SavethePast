#Setup#
import pygame
from pygame.locals import *
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
pygame.display.set_caption('Save the Past')
done = False
white = (255,255,255)
limegreen = (50, 205, 50)
lime = (0,255,0)
black = (0,0,0)
worldx=800
worldy=800
done = False
world = pygame.display.set_mode([worldx,worldy])
pygame.display.set_caption("Pollution")
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
              print(event)
              if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        ButtonStart("play")
        pygame.display.flip()
        clock.tick(15)
        ButtonSelection()
        pygame.display.flip()
        clock.tick(15)
        Water()
        Outside()
def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()
def ButtonStart(action=None):
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and action != None:
        pygame.display.update()
        pygame.time.wait(100)
        pygame.display.flip()
        image = pygame.image.load('tree.png').convert()
        world.blit(image,[0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite() # create sprite
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [-50, 350] # put the ball in the top left corner
        world.blit(d.image, d.rect)
        pygame.display.flip()
        v = pygame.sprite.Sprite()
        v.image = pygame.image.load("vanessathechar.png").convert_alpha()
        v.rect = v.image.get_rect()
        v.rect.topleft = [500,400]
        world.blit(v.image, v.rect)
def ButtonSelection():
    keys=pygame.key.get_pressed()
    if keys [pygame.K_v]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('Prebath.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        v = pygame.sprite.Sprite()
        v.image = pygame.image.load("vanessathechar.png").convert_alpha()
        v.rect = v.image.get_rect()
        v.rect.topleft = [300,450]
        world.blit(v.image, v.rect)
    elif keys [pygame.K_d]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('Prebath.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite() # create sprite
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [300, 400] # put the ball in the top left corner
        world.blit(d.image, d.rect)
        pygame.display.flip()
def Water():
    keys=pygame.key.get_pressed()
    #How to make paths for different sprites. A path for Vanessa and one for Dave
    if keys [pygame.K_w]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('Postbath.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        v = pygame.sprite.Sprite()
        v.image = pygame.image.load("vanessathechar.png").convert_alpha()
        v.rect = v.image.get_rect()
        v.rect.topleft = [300,450]
        world.blit(v.image, v.rect)
    elif keys [pygame.K_r]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('Postbath.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite() # create sprite
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [300, 400] # put the ball in the top left corner
        world.blit(d.image, d.rect)
        pygame.display.flip()

def Outside():
    keys=pygame.key.get_pressed()
    if keys [pygame.K_o]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('trash.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        v = pygame.sprite.Sprite()
        v.image = pygame.image.load("vanessathechar.png").convert_alpha()
        v.rect = v.image.get_rect()
        v.rect.topleft = [300,275]
        world.blit(v.image, v.rect)
    if keys [pygame.K_b]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('trash.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite() # create sprite
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [300, 230] # put the ball in the top left corner
        world.blit(d.image, d.rect)
        pygame.display.flip()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((325),(200))
    world.blit(TextSurf, TextRect)
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


game_intro()
