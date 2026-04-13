import pygame
pygame.init()
HEIGHT=600
WIDTH=1000
screen= pygame.display.set_mode((WIDTH,HEIGHT))
load1=pygame.image.load("space shooter/images/space.png")
load2=pygame.image.load("space shooter/images/spaceship_red.png")
load3=pygame.image.load("space shooter/images/spaceship_yellow.png")
border=pygame.Rect(495,0,10,600)
while True:
    screen.blit(load1,(0,0))
    pygame.draw.rect(screen,"black",border)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()