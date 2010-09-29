from copy import copy
import pygame,sys
from pygame.locals import *
from pygame.sprite import Sprite, RenderUpdates
def drawinit():
    pygame.init()
    global screen
    screen = pygame.display.set_mode( ( 640, 480 ) )
    pygame.display.set_caption("*****O auto da compadecida*****")
def draw(image,(x,y)):
    screen.blit(image,(x,y))
    
