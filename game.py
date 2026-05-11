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
RS=pygame.Rect(692,300,60,60)
shoot=pygame.mixer.Sound("space shooter/images/Gun+Silencer.mp3")
shot=pygame.mixer.Sound("space shooter/images/Grenade+1.mp3")
YB=[]
RB=[]
RH=10
YH=10
def YR():
    if keys_pressed[pygame.K_w] and YS.y>0:
        YS.y-=2.5
    if keys_pressed[pygame.K_a] and YS.x>0:
        YS.x-=2.5
    if keys_pressed[pygame.K_s] and YS.y<540:
        YS.y+=2.5
    if keys_pressed[pygame.K_d] and YS.x<435:
        YS.x+=2.5
def RR():
    if keys_pressed[pygame.K_UP] and RS.y>0:
        RS.y-=2.5
    if keys_pressed[pygame.K_LEFT] and RS.x>505:
        RS.x-=2.5
    if keys_pressed[pygame.K_DOWN] and RS.y<540:
        RS.y+=2.5
    if keys_pressed[pygame.K_RIGHT] and RS.x<940:
        RS.x+=2.5
clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    screen.blit(load1,(0,0))
    pygame.draw.rect(screen,"black",border)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL:
                shoot.play()
                bullet2=pygame.Rect(RS.x-20,RS.y+25,20,10)
                RB.append(bullet2)
            if event.key == pygame.K_SPACE:
                shoot.play() 
                bullet=pygame.Rect(YS.x+60,YS.y+25,20,10)
                YB.append(bullet)
    keys_pressed = pygame.key.get_pressed()
    YR()
    RR()
    screen.blit(load3R,YS)
    screen.blit(load2R,RS)
    Ytext=font1.render("health "+str(YH),True,"white")
    Rtext=font1.render("health "+str(RH),True,"white")
    screen.blit(Ytext,(10,10))  
    screen.blit(Rtext,(860,10)) 
    for bullet in YB:
        pygame.draw.rect(screen,"Yellow",bullet)
        bullet.x+=2
        if bullet.colliderect(RS):
            RH-=1
            YB.remove(bullet)
            shot.play()
    if YH<=0:
        screen.fill("red")
        Rwin=font1.render("Red wins",True,"black")
        screen.blit(Rwin,(500,300))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit
    for bullet in RB:
        pygame.draw.rect(screen,"red",bullet)
        bullet.x-=3
        if bullet.colliderect(YS):
            YH-=1
            RB.remove(bullet)
            shot.play()
    if RH<=0:
        screen.fill("Yellow")
        Ywin=font1.render("Yellow wins",True,"black")
        screen.blit(Ywin,(500,300))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()

    pygame.display.update()