import pygame
pygame.init()
HEIGHT=600
WIDTH=1000
FPS = 60
screen= pygame.display.set_mode((WIDTH,HEIGHT))
load1=pygame.image.load("space shooter/images/space.png")
load2=pygame.image.load("space shooter/images/spaceship_red.png")
load3=pygame.image.load("space shooter/images/spaceship_yellow.png")
font1=pygame.font.SysFont("segoeuiemoji",30)
border=pygame.Rect(495,0,10,600)
load2S=pygame.transform.scale(load2,(60,60))
load3S=pygame.transform.scale(load3,(60,60))
load2R=pygame.transform.rotate(load2S,270)
load3R=pygame.transform.rotate(load3S,90)
YS=pygame.Rect(248,300,60,60)
RS=pygame.Rect(753,300,60,60)
def YR():
    if keys_pressed[pygame.K_w] and YS.y>0:
        YS.y-=2.5
    if keys_pressed[pygame.K_a] and YS.x>0:
        YS.x-=2.5
    if keys_pressed[pygame.K_s] and YS.y<540:
        YS.y+=2.5
    if keys_pressed[pygame.K_d] and YS.x<435:
        YS.x+=2.5
clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    screen.blit(load1,(0,0))
    pygame.draw.rect(screen,"black",border)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
    keys_pressed = pygame.key.get_pressed()
    YR()
    screen.blit(load3R,YS)
    screen.blit(load2R,RS)
    Ytext=font1.render("health ",True,"white")
    Rtext=font1.render("health ",True,"white")
    screen.blit(Ytext,(10,10))  
    screen.blit(Rtext,(860,10)) 
    pygame.display.update()