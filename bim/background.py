from copy import copy
import pygame,sys,os
from pygame.locals import *
from pygame.sprite import Sprite, RenderUpdates
from draw import *
class Background:
    def __init__(self):
        self.img = pygame.image.load(os.path.join("img","fundo.jpg"))
        self.imgSky = pygame.image.load(os.path.join("img",'ceu.jpg'))
        self.imgRapadura = pygame.image.load(os.path.join("img",'rapadura.png'))
        self.font = pygame.font.Font(pygame.font.match_font(pygame.font.get_default_font()),25)
        self.pos = pygame.Rect((0,140,6400,340))
        self.score = self.font.render("",1,(0,0,0))
        self.actived = 0
        draw(self.img,(self.pos.left,self.pos.top))
    def move(self,key):
        if key == 275:
            self.pos.move_ip(-10,0)
            if self.pos.left == -5770:
                self.background2 = Background()                    
                self.background2.pos.move_ip(640,0)
                self.actived = 1
            if self.actived:
                self.background2.pos.move_ip(-10,0)                   
                if not self.background2.pos.left:
                    self.transfer()
                    self.actived = 0       
        if key == 276:
            self.pos.move_ip(10,0)
            if self.pos.left == 10:
                self.background2 = Background()
                self.background2.pos.move_ip(-1280,0)
                self.actived = 1
            if self.actived:
                self.background2.pos.move_ip(10,0)
                if not self.background2.pos.right:
                    self.transfer()
                    self.actived = 0
    def transfer(self):
        self.pos = self.background2.pos
    def redraw(self):
        draw(self.img,(self.pos.left,self.pos.top))
        if self.actived:
            draw(self.background2.img,(self.background2.pos.left,self.background2.pos.top))
        draw(self.score,(500,140))
    def sky(self):
        draw(self.imgSky,(0,0))
        
        
                
        
        
