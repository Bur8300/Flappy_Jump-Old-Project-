import pygame
import time
import math
import random

genislik=400
yükseklik=600
screen=pygame.display.set_mode((genislik,yükseklik))
clock=pygame.time.Clock()


WalkLeft=[pygame.image.load("bird1Left.png"),pygame.image.load("bird2Left.png"),pygame.image.load("bird3Left.png")]
WalkRight=[pygame.image.load("bird1.png"),pygame.image.load("bird2.png"),pygame.image.load("bird3.png")]
background=pygame.image.load("bg.png")
char=[pygame.image.load("bird1.png"),pygame.image.load("bird1Left.png")]
background=pygame.transform.scale(background,(400,600))

class player(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.isJump=False
        self.Collid=False
        self.JumpCount=11
        self.WalkCount=0
        self.right=False
        self.left=False
        self.direction=False
        self.width=34
        self.height=24
        self.hitbox = (self.x,self.y,self.width,self.height)

    def drawGameWindow(self,screen):

        if self.WalkCount + 1 >=7:
            self.WalkCount=0


        if self.right == True and self.left ==False:
            screen.blit(WalkRight[self.WalkCount//3],(self.x,self.y))
            self.WalkCount += 1   
        elif self.left == True and self.right ==False:
            screen.blit(WalkLeft[self.WalkCount//3],(self.x,self.y))
            self.WalkCount += 1
        else:
            if self.direction== False:
                screen.blit(char[0],(self.x,self.y))
            else:
                screen.blit(char[1],(self.x,self.y))                
        self.hitbox = (self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen,(255,0,0),self.hitbox,1)



def redrawGameWindow():
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,(255,0,0),(150,400,100,10)) 
    Bird.drawGameWindow(screen)           
    pygame.display.flip()

Bird = player(200,400)
runnning = True
while runnning:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
    if 120<Bird.x<250 and 386>=Bird.y>=376:
        Bird.Collid=True 

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        Bird.x-=15
        Bird.left=True
        Bird.right=False
        Bird.direction=True
    elif keys[pygame.K_RIGHT]:
        Bird.x+=15
        Bird.right=True
        Bird.left=False
        Bird.direction=False
    else:
        Bird.WalkCount=0
    if Bird.isJump == False and Bird.Collid == False:
        if Bird.y <575:
            Bird.y+=10
        if Bird.y >= 576:
            Bird.y =575
        if keys[pygame.K_UP]:
            Bird.isJump=True
    else:
        if Bird.JumpCount>=0:    
            Bird.y-=(Bird.JumpCount ** 2) * 0.5 
            Bird.JumpCount-=1
        else:
            Bird.isJump= False
            Bird.Collid=False
            Bird.JumpCount=11

       
    


    if Bird.x>384:
        Bird.x=-20
    if Bird.x<-20:
        Bird.x=364
    redrawGameWindow()
    clock.tick(60)