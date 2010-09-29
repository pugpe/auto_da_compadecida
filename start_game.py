from copy import copy
import pygame,sys
sys.path.append("bim")
from pygame.locals import *
from pygame.sprite import Sprite, RenderUpdates
from avata import Avata
from draw import *
drawinit()
joao = Avata()
clock = pygame.time.Clock()
key = 0
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            key = event.key
        elif event.type == KEYUP:
            keyUP = event.key
            if not (keyUP == 32 or keyUP == 273):
                key = 0
    joao.move(key)
    if key == 32 or key == 273: key = lastKey
    else: lastKey = key
    pygame.display.flip()
