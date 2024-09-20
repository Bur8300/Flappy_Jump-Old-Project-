import pygame
import time
import math
import random

genislik=400
yükseklik=600
screen=pygame.display.set_mode((genislik,yükseklik))
pygame.display.set_caption("Flappy JUMP")
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

class projectile(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.hitbox = (self.x,self.y,self.width,self.height)

    def draw(self,screen):
        self.hitbox = (self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.width, self.height))  




def redrawGameWindow():
    screen.blit(background,(0,0))
    for brick in bricks:
        brick.draw(screen)

    Bird.drawGameWindow(screen)           
    pygame.display.flip()

brick1=projectile(random.randint(0,300),0,100,20)
brick2=projectile(random.randint(0,300),125,100,20)
brick3=projectile(random.randint(0,300),250,100,20)
brick4=projectile(random.randint(0,300),375,100,20)
brick5=projectile(random.randint(0,300),500,100,20)
bricks=[brick1,brick2,brick3,brick4,brick5]







Bird = player(200,400)
runnning = True
while runnning:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

    for brick in bricks:
        if brick.x-34 < Bird.x < brick.x+120 and brick.y-34<=Bird.y<=brick.y-24:
            Bird.Collid=True

        if brick.y < 591:
            brick.y += brick.vel
        else:
            brick.y = 0
            brick.x = random.randint(0,300)
            brick.vel= random.randint(2,5)



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
            runnning=False
            
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


        
    

    if Bird.y<=0:
        Bird.y=0
    if Bird.x>384:
        Bird.x=-20
    if Bird.x<-20:
        Bird.x=364
    redrawGameWindow()

    clock.tick(30)
