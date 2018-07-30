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
              #print(event)
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
        Lights()
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
    if keys [pygame.K_d]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('Prebath.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite() # create sprite
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [300,450] # put the ball in the top left corner
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
        print("Americans now use 127 percent more water than we did in 1950.")
        print("About 95 percent of the water entering our homes goes down the drain.")
        print("Running the tap while brushing your teeth can waste 4 gallons of water.")
        print("Older toilets can use 3 gallons of clean water with every flush, while new toilets use as little as 1 gallon.")
        print("Leaky faucets that drip at the rate of one drop per second can waste up to 2,700 gallons of water each year.")
        print("A garden hose or sprinkler can use almost as much water in an hour as an average family of four uses in one day.")
        print("A water-efficient dishwasher will use as little a 4 gallons per wash cycle, whereas some older models use up to 13 gallons per cycle.")
        print("Some experts estimate that more than 50 percent of landscape water use goes to waste due to evaporation or runoff caused by over-watering.")
        print("Many people in the world exist on 3 gallons of water per day or less. We can use that amount in one flush of the toilet.")
        print("Over a quarter of all the clean, drinkable water you use in your home is used to flush the toilets.")
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
        print("Americans now use 127 percent more water than we did in 1950.")
        print("About 95 percent of the water entering our homes goes down the drain.")
        print("Running the tap while brushing your teeth can waste 4 gallons of water.")
        print("Older toilets can use 3 gallons of clean water with every flush, while new toilets use as little as 1 gallon.")
        print("Leaky faucets that drip at the rate of one drop per second can waste up to 2,700 gallons of water each year.")
        print("A garden hose or sprinkler can use almost as much water in an hour as an average family of four uses in one day.")
        print("A water-efficient dishwasher will use as little a 4 gallons per wash cycle, whereas some older models use up to 13 gallons per cycle.")
        print("Some experts estimate that more than 50 percent of landscape water use goes to waste due to evaporation or runoff caused by over-watering.")
        print("Many people in the world exist on 3 gallons of water per day or less. We can use that amount in one flush of the toilet.")
        print("Over a quarter of all the clean, drinkable water you use in your home is used to flush the toilets.")
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

def Lights():
    keys=pygame.key.get_pressed()
    if keys [pygame.K_l]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('led.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        v = pygame.sprite.Sprite()
        v.image = pygame.image.load("vanessathechar.png").convert_alpha()
        v.rect = v.image.get_rect()
        v.rect.topleft = [300,275]
        world.blit(v.image, v.rect)
        print("Compared to traditional incandescents, energy-efficient lightbulbs such as halogen incandescents, compact fluorescent lamps (CFLs), and light emitting diodes (LEDs) have the following advantages: \nTypically use about 25-80 percent less energy than traditional incandescents, saving you money and can last 3-25 times longer.")
        print("")
    if keys [pygame.K_c]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('led.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite() # create sprite
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [300, 230] # put the ball in the top left corner
        world.blit(d.image, d.rect)
        pygame.display.flip()

# def message_display(text):
#     largeText = pygame.font.Font('freesansbold.ttf',30)
#     TextSurf, TextRect = text_objects(text, largeText)
#     TextRect.center = ((325),(200))
#     world.blit(TextSurf, TextRect)

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
