import pygame
import random

pygame.init()

#Ekran
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Deneme")

icon=pygame.image.load("spidey3.png")
pygame.display.set_icon(icon)



spaceship =pygame.image.load("spaceship.png")
playerx=350
playery=400
playerxc=0
playeryc=0

ufo = pygame.image.load("ufo.png")
ufox=random.randint(0,800)
ufoy=random.randint(0,50)
ufoxc=0.25
ufoyc=0.05


def player(a,x,y):
    screen.blit(a,(x,y))



#Loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxc=-0.5
            if event.key == pygame.K_RIGHT:
                playerxc=0.5
            if event.key == pygame.K_UP:
                playeryc=-0.5
            if event.key == pygame.K_DOWN:
                playeryc=0.5   
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerxc=0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playeryc=0
        if event.type == pygame.QUIT:
            running = False
    
    if ufox>736:
        ufoxc=-(ufoxc)
    if ufox<0:
        ufoxc=-(ufoxc)
    if ufoy>536:
        ufoyc=-(ufoyc)
    if ufoy<0:
        ufoyc=-(ufoyc)
    
    
    playerx+=playerxc
    playery+=playeryc        
    if playerx<=0:
        playerx=0
    if playerx>=715:
        playerx=715
    

    ufox+=ufoxc
    ufoy+=ufoyc


    screen.fill((0,0,0))
    player(spaceship,playerx,playery)
    player(ufo,ufox,ufoy)
    pygame.display.flip()
    clock.tick(1200)