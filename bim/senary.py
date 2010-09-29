from copy import copy
import pygame,sys,os
from pygame.locals import *
from pygame.sprite import Sprite, RenderUpdates
from draw import *
from background import *
from fire import Fire
from background import Background
class Senary:
    def __init__(self):
        self.file = open(os.path.join("bd",'level1.txt'),'r')
        self.imgStone = pygame.image.load(os.path.join("img",'stone.png'))
        self.imgInimigo = pygame.image.load(os.path.join("img",'inimigo1.png'))
        self.imgInimigo2 = pygame.image.load(os.path.join("img",'inimigo2.png'))
        self.imgLife = pygame.image.load(os.path.join("img",'rapadura.png'))
        self.imgStone.set_colorkey((10,255,0),0)
        self.imgStone.set_alpha(255,0)
        self.imgInimigo.set_colorkey((255,0,0),0)
        self.imgInimigo.set_alpha(255,0)
        self.contIA = 0
        self.shot = Fire()
        self.stone = []
        self.inimigo = []
        self.inimigoDir = []
        self.inimigoLife = []
        self.inimigoStep = []
        self.life = []
        self.pos = []
        for i in range(269):
            self.pos.append(int(self.file.read(1)))
            if self.pos[i]:
                self.constructor(i)
    def constructor(self,pos):
        if self.pos[pos] == 1:
            self.stone.append(pygame.Rect(pos*40,360,40,80))
        if self.pos[pos] == 2:
            self.inimigo.append(pygame.Rect(pos*40,320,40,120))
            self.inimigoDir.append(-1)
            self.inimigoStep.append(-1)
            self.inimigoLife.append(2)
        if self.pos[pos] == 3:
            self.life.append(pygame.Rect(pos*40,380,40,40))
    def draw(self):
        for i in range(len(self.stone)-1):
            draw(self.imgStone,(self.stone[i].left,self.stone[i].top))
        for i in range(len(self.inimigo)-1):
            if self.inimigoStep[i] == 1:
                draw(self.imgInimigo,(self.inimigo[i].left,self.inimigo[i].top))
            else:
                draw(self.imgInimigo2,(self.inimigo[i].left,self.inimigo[i].top))
        for i in range(len(self.life)-1):
            draw(self.imgLife,(self.life[i].left,self.life[i].top))    
    def move(self,x):
        for i in range(len(self.stone)-1):
            self.stone[i].move_ip(x*10,0)
        for i in range(len(self.inimigo)-1):
            self.inimigoStep[i] *=-1
            self.inimigo[i].move_ip(x*10,0)
        for i in range(len(self.life)-1):
            self.life[i].move_ip(x*10,0)
    def constructorAdd(self,x):
        if x == 0:
            self.inimigo.append(pygame.Rect(640,320,40,120))
            self.inimigoDir.append(-1)
            self.inimigoLife.append(5)
            self.inimigoStep.append(1)
        elif x == 1:
            self.life.append(pygame.Rect(640,380,40,40))
