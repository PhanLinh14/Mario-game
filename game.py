import pygame, sys
from mario import Mario
from pygame.locals import *

pygame.init()
WIDTHWD= 800
HEIGHTWD= 600

FPS = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTHWD,HEIGHTWD))
BACKGROUND= pygame.image.load('img/background.png')
icon= pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Super Mario Brother')

mario = Mario(0, HEIGHTWD - (65+35)) 
active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(mario)

def start_screen():
    screen.blit(pygame.image.load('img/bck.png'), (0, 0))
    pygame.display.flip()
    continues = True
    while continues:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                continues = False
            if event.type == pygame.QUIT:
                terminate()
    main()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and mario.rect.x > 0:
            mario.move_left()
        elif keys[pygame.K_RIGHT] and mario.rect.x < (WIDTHWD - mario.image.get_width()):
            mario.move_right()
        elif not mario.isJumping:
            if keys[pygame.K_SPACE]:
                mario.jump()
                
        active_sprite_list.update()
        screen.blit(BACKGROUND, (0,0))
        active_sprite_list.draw(screen)
        pygame.display.update()
        
        fpsClock.tick(FPS)

def terminate(): 
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()

start_screen()