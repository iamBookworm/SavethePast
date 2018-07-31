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
        Recycle()
        Compost()
        End()
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
    #     print("Americans now use 127 percent more water than we did in 1950.")
    #     print("About 95 percent of the water entering our homes goes down the drain.")
    #     print("Running the tap while brushing your teeth can waste 4 gallons of water.")
    #     print("Many people in the world exist on 3 gallons of water per day or less. We can use that amount in one flush of the toilet.")
    if keys [pygame.K_r]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('Postbath.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite()
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [300, 450] # put the ball in the top left corner
        world.blit(d.image, d.rect)
        pygame.display.flip()
        # print("Americans now use 127 percent more water than we did in 1950.")
        # print("About 95 percent of the water entering our homes goes down the drain.")
        # print("Running the tap while brushing your teeth can waste 4 gallons of water.")
        # print("Many people in the world exist on 3 gallons of water per day or less. We can use that amount in one flush of the toilet.")
def Outside():
    keys=pygame.key.get_pressed()
    if keys [pygame.K_o]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('vanessaled.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        v = pygame.sprite.Sprite()
        v.image = pygame.image.load("vanessathechar.png").convert_alpha()
        v.rect = v.image.get_rect()
        v.rect.topleft = [300,275]
        world.blit(v.image, v.rect)
        print("Americans now use 127 percent more water than we did in 1950.")
        print("About 95 percent of the water entering our homes goes down the drain.")
        print("Running the tap while brushing your teeth can waste 4 gallons of water.")
        print("Many people in the world exist on 3 gallons of water per day or less. We can use that amount in one flush of the toilet.")
    if keys [pygame.K_b]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('daveled.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite() # create sprite
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [300, 230] # put the ball in the top left corner
        world.blit(d.image, d.rect)
        pygame.display.flip()
        print("Americans now use 127 percent more water than we did in 1950.")
        print("About 95 percent of the water entering our homes goes down the drain.")
        print("Running the tap while brushing your teeth can waste 4 gallons of water.")
        print("Many people in the world exist on 3 gallons of water per day or less. We can use that amount in one flush of the toilet.")

def Lights():
    keys=pygame.key.get_pressed()
    if keys [pygame.K_l]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('vanessarecycle.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        v = pygame.sprite.Sprite()
        v.image = pygame.image.load("vanessathechar.png").convert_alpha()
        v.rect = v.image.get_rect()
        v.rect.topleft = [300,275]
        world.blit(v.image, v.rect)
        # print("Compared to traditional incandescents, energy-efficient lightbulbs such as halogen incandescents, compact fluorescent lamps (CFLs), and light emitting diodes (LEDs) have the following advantages: \nTypically use about 25-80 percent less energy than traditional incandescents, saving you money and can last 3-25 times longer.")
        # print("Today’s CFL models have gone through a major makeover. They are smaller, more reasonably priced, save a lot more energy than traditional incandescent bulbs and last longer.")
        # print("CFLs can last up to 10 times longer than incandescent bulbs, saving on production and disposal costs.")
        # print("CFLs use up to 75 percent less energy than traditional incandescent bulbs.")
    if keys [pygame.K_c]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('daverecycle.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite() # create sprite
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [300, 230] # put the ball in the top left corner
        world.blit(d.image, d.rect)
        pygame.display.flip()
        # print("Compared to traditional incandescents, energy-efficient lightbulbs such as halogen incandescents, compact fluorescent lamps (CFLs), and light emitting diodes (LEDs) have the following advantages: \nTypically use about 25-80 percent less energy than traditional incandescents, saving you money and can last 3-25 times longer.")
        # print("Today’s CFL models have gone through a major makeover. They are smaller, more reasonably priced, save a lot more energy than traditional incandescent bulbs and last longer.")
        # print("CFLs can last up to 10 times longer than incandescent bulbs, saving on production and disposal costs.")
        # print("CFLs use up to 75 percent less energy than traditional incandescent bulbs.")
def Recycle():#Pic
    keys=pygame.key.get_pressed()
    if keys [pygame.K_i]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('compostvanessa.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        v = pygame.sprite.Sprite()
        v.image = pygame.image.load("vanessathechar.png").convert_alpha()
        v.rect = v.image.get_rect()
        v.rect.topleft = [300,275]
        world.blit(v.image, v.rect)
        # print("Recycled paper produces 73% less air pollution than if it was made from raw materials.")
        # print("Americans use 85,000,000 tons of paper a year; about 680 pounds per person.")
        # print("The total generation of municipal solid waste in 2014 was 258.5 million tons,  approximately 3.5 million tons more than the amount generated in 2013.")
    if keys [pygame.K_j]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('compostdave.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite() # create sprite
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [300, 230] # put the ball in the top left corner
        world.blit(d.image, d.rect)
        pygame.display.flip()
#         print("Recycled paper produces 73% less air pollution than if it was made from raw materials.")
#         print("Americans use 85,000,000 tons of paper a year; about 680 pounds per person.")
#         print("The total generation of municipal solid waste in 2014 was 258.5 million tons,  approximately 3.5 million tons more than the amount generated in 2013.")
def Compost():
    keys=pygame.key.get_pressed()
    if keys [pygame.K_q]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('compost.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        v = pygame.sprite.Sprite()
        v.image = pygame.image.load("vanessathechar.png").convert_alpha()
        v.rect = v.image.get_rect()
        v.rect.topleft = [300,275]
        world.blit(v.image, v.rect)
        print("Each year the average American throws away approximately 1,200 lbs of organic waste which includes grass, leaves, tree trimming and food waste that can be composted.")
        print("70% of the worlds waste can be composted.")
        print("On average it costs $35 per ton to compost waste, $50 per ton to landfill it and up to $75 per ton to incinerate it.")
    if keys [pygame.K_p]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('compost.png').convert()
        world.blit(image, [0,0])
        pygame.display.flip()
        d = pygame.sprite.Sprite() # create sprite
        d.image = pygame.image.load("300dave.png").convert_alpha() # load ball image
        d.rect = d.image.get_rect() # use image extent values
        d.rect.topleft = [300, 230] # put the ball in the top left corner
        world.blit(d.image, d.rect)
        pygame.display.flip()
        print("Each year the average American throws away approximately 1,200 lbs of organic waste which includes grass, leaves, tree trimming and food waste that can be composted.")
        print("70% of the worlds waste can be composted.")
        print("On average it costs $35 per ton to compost waste, $50 per ton to landfill it and up to $75 per ton to incinerate it.")
def End():
    keys=pygame.key.get_pressed()
    if keys [pygame.K_e]:
        pygame.display.update()
        pygame.time.wait(10)
        pygame.display.flip()
        image = pygame.image.load('finalimage.png').convert()
        world.blit(image, [0,0])
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
