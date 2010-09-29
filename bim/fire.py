from copy import copy
import pygame,sys,os
from pygame.locals import *
from pygame.sprite import Sprite, RenderUpdates
from draw import *
class Fire():
    def __init__(self):
        self.img = pygame.Surface((15,15))
        self.img = pygame.image.load(os.path.join("img","moeda.png"))
        self.img2 = pygame.image.load(os.path.join("img","tiro.jpg"))
        self.img.set_colorkey((10,255,0),0)
        self.img.set_alpha(255,0)
        self.dir = []
        self.pos = []
        self.origem = []
    def fire(self,(x,y),direction,ini):       
        self.dir.append(direction)
        self.origem.append(ini)
        if direction:
            self.pos.append(pygame.Rect(x+41,y,10,10))
        else:
            self.pos.append(pygame.Rect(x-41,y,10,10))
    def move(self):
        i=-1
        while i != len(self.dir)-1:
            i+=1
            if self.origem[i]:
                draw(self.img,(self.pos[i].left,self.pos[i].top))
            else:
                draw(self.img2,(self.pos[i].left,self.pos[i].top))
            if self.dir[i]:
                self.pos[i].move_ip(15,0)
                if self.pos[i].left == 640:
                    self.dir.pop(i)
                    self.pos.pop(i)
                    self.origem.pop(ini)
                    i-=1
            else:
                self.pos[i].move_ip(-15,0)
                if not self.pos[i].left:
                    self.dir.pop(i)
                    self.pos.pop(i)
                    self.origem.pop(ini)
                    i-=1
            
        
