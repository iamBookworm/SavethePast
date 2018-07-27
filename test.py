# import pygame
import pygame
from pygame import *
import tkinter
from tkinter import *
import sys
import os
import time
import random
# initialize game engine
pygame.init()
window_width=800
window_height=800

animation_increment=10
clock_tick_rate=20
fps= 40
ani = 4
clock= pygame.time.Clock()
#Different Colors
white = (255,255,255)
black = (0,0,0)
worldx=800
worldy=800
done = False

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("3 items you can change?")

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("trash.png").convert()

while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)
