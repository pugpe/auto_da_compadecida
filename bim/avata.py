from copy import copy
import pygame,sys,random,os
from pygame.locals import *
from pygame.sprite import Sprite, RenderUpdates
from draw import *
from background import *
from fire import Fire
from background import Background
from senary import Senary
class Avata:
    def __init__(self):
        self.background = Background()
        self.shot = Fire()
        self.senary = Senary()
        self.trilha = pygame.mixer.Sound(os.path.join("sound","trilha.wav"))
        self.tiro = pygame.mixer.Sound(os.path.join("sound",'tiro.wav'))
        self.porrada = pygame.mixer.Sound(os.path.join("sound",'porrada.wav'))
        self.morreu = pygame.mixer.Sound(os.path.join("sound",'morreu.wav'))
        self.trilha.play(-1)
        self.img = pygame.Surface((80,120))
        self.img = pygame.image.load(os.path.join("img",'joao1.png'))
        self.imgS = pygame.image.load(os.path.join("img",'joao2.png'))
        self.imgC = pygame.image.load(os.path.join("img",'joao1c.png'))
        self.imgSC = pygame.image.load(os.path.join("img",'joao2c.png'))
        self.img.set_colorkey((10,255,0),0)
        self.img.set_alpha(255,0)
        self.img2 = pygame.Surface((80,120))
        self.img2.set_colorkey((10,255,0),0)
        self.img2.set_alpha(255,0)
        self.pos = pygame.Rect((120,320,80,120))
        self.jump = 0
        self.jump_h = 11
        self.life = 5
        self.face = 1
        self.x = 0
        self.contx = 0
        self.step = 1
        self.score = 0
        self.moveActivedJump = 1 
        draw(self.img,(self.pos.left,self.pos.top))
        self.background.sky()
        self.drawLife()
    def move(self,key):
        self.background.redraw()
        if key == 273 and (self.jump_h == 11 or not self.moveActivedJump):
            self.jump = 1
            if self.moveActivedJump:
                self.jump_h = 0
            else:
                self.jump_h = 4
        elif key == 275:
            self.moveActived = 1
            self.step *= -1
            for i in range(len(self.senary.stone)-1):
                if self.pos.collidepoint(self.senary.stone[i].left-10,self.senary.stone[i].top):
                    self.moveActived = 0
            if self.moveActived:
                if self.pos.left >= 200:
                    self.background.move(key)
                    self.senary.move(-1)
                else:
                    self.pos.move_ip(10,0)
                self.face = 1
        elif key == 276:
            self.moveActived = 1
            self.step *= -1
            for i in range(len(self.senary.stone)-1):
                if self.pos.collidepoint(self.senary.stone[i].right,self.senary.stone[i].top):
                    self.moveActived = 0
            if self.moveActived:
                if self.pos.left == 100:
                    self.background.move(key)
                    self.senary.move(1)
                else:
                    self.pos.move_ip(-10,0)
                self.face = 0
        if self.jump:
            self.pos.move_ip(0,-20)
        if self.jump_h < 10: self.jump_h +=1
        self.moveActivedJump = 1
        for i in range(len(self.senary.stone)-1):
            if self.pos.collidepoint(self.senary.stone[i].right,self.senary.stone[i].top-10) or self.pos.collidepoint(self.senary.stone[i].left,self.senary.stone[i].top-10):
                self.moveActivedJump = 0
        if self.jump_h == 10 and self.moveActivedJump:
            if self.pos.top < 320:
                self.pos.move_ip(0,20)
            else : self.jump_h += 1
            self.jump = 0
        if key == 32:
            self.tiro.play()
            self.shot.fire(self.pos.center,self.face,1)
        self.ia()
        if len(self.shot.dir):
            self.shot.move()
            i=-1
            while i != len(self.shot.dir)-1:
                i+=1
                for j in range(len(self.senary.stone)-1):
                    if self.shot.pos[i].colliderect(self.senary.stone[j]):
                        self.shot.dir.pop(i)
                        self.shot.pos.pop(i)
                        self.shot.origem.pop(i)
                        i-=1
                        break
            i=-1
            while i != len(self.shot.dir)-1:
                i+=1 
                for j in range(len(self.senary.inimigo)-1):
                    if self.shot.pos[i].colliderect(self.senary.inimigo[j]) and self.shot.origem[i]:
                        self.senary.inimigoLife[j] -=1
                        self.score += 50
                        if not self.senary.inimigoLife[j]:
                            self.senary.inimigo.pop(j)
                            self.senary.inimigoLife.pop(j)
                            self.senary.inimigoDir.pop(j)
                            self.senary.inimigoStep.pop(j)
                            self.score += 300
                        self.shot.dir.pop(i)
                        self.shot.pos.pop(i)
                        self.shot.origem.pop(i)
                        self.background.score = self.background.font.render(str(self.score),1,(0,0,0))
                        i-=1
                        break
            i=-1
            while i != len(self.shot.dir)-1:
                i+=1
                if self.shot.pos[i].colliderect(self.pos):
                    self.shot.dir.pop(i)
                    self.shot.pos.pop(i)
                    self.shot.origem.pop(i)
                    self.lifes()
                    i-=1
                    break
        if len(self.senary.life):
            for i in range(len(self.senary.life)-1):
                if self.senary.life[i].colliderect(self.pos):
                    self.senary.life.pop(i)
                    self.life+=5
                    self.lifes()
                    break
        if self.face:
            if self.step == 1:
                draw(self.img,(self.pos.left,self.pos.top))
            else:
                draw(self.imgS,(self.pos.left,self.pos.top))
        else:
            if self.step == 1:
                draw(self.imgC,(self.pos.left,self.pos.top))
            else:
                draw(self.imgSC,(self.pos.left,self.pos.top))
        rand = random.randint(0,80)
        if rand > 76 and rand < 79:
            self.senary.constructorAdd(0)
        elif rand == 80:
            self.senary.constructorAdd(1)
        self.senary.draw()
        if self.senary.stone[0].left == -2700:
                self.senary.move(350)
    def lifes(self):
        self.porrada.play()
        self.life -= 1
        self.background.sky()
        self.drawLife()
        if self.life == 0:
                self.dead()
    def ia(self):
        self.senary.contIA+=1
        if not self.senary.contIA % 10:
            for i in range(len(self.senary.inimigo)-1):
                self.inimigoGO = 1
                for j in range(len(self.senary.stone)-1):
                    if self.senary.inimigo[i].colliderect(self.senary.stone[j]):
                        self.inimigoGO = 0
                        break
                if not self.inimigoGO:
                    self.senary.inimigoDir[i]*=-1
                self.senary.inimigoStep[i] *=-1
                self.senary.inimigo[i].move_ip(10*self.senary.inimigoDir[i],0)
        if self.senary.contIA == 50:
            for i in range(len(self.senary.inimigo)-1):
                self.shot.fire(self.senary.inimigo[i].center,0,0)
            self.senary.contIA = 0
    def drawLife(self):
        for i in range(self.life):
            draw(self.background.imgRapadura,(50*i+20,40))
    def dead(self):
        key = 0
        self.trilha.stop()
        self.morreu.play()
        while(key!=13):
            for event in pygame.event.get():
                if  event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    key = event.key            
        sys.exit()
                
                
