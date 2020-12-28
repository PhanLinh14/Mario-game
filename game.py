import pygame, sys, constants, platform
from cactus import Cactus
from coin import Coin
from cube import Cube
from mario import Mario
from pygame.locals import *

pygame.init()
# The font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)

FPS = 60
# Used to manage how fast the screen updates
fpsClock = pygame.time.Clock()

#set up screen
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
BACKGROUND= pygame.image.load('img/background.png')
icon= pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Super Mario Brother')

sprites = [
            #stay
            pygame.image.load('img/mario.png'),
            #1, run1
            pygame.image.load('img/run1.png'),
            #2, run left
            pygame.image.load('img/run1L.png'),
            #3, jump
            pygame.image.load('img/jump.png') ]

#create lists for all sprites and coins
active_sprite_list = pygame.sprite.Group()
# initialize player
player = Mario(0,500)
cube1 = Cube(200, 300)
cube2 = Cube(450, 270)
coin1 = Coin(200, 300)
coin2 = Coin(450, 270)
# player.rect.x = 0
# player.rect.y = 600
active_sprite_list.add(player, cube1, cube2)
# Collision temp variable
collideCube1 = False
collideCube2 = False

level1coin_list = pygame.sprite.Group()
level1cactus_list = pygame.sprite.Group()

#Draw text function           
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, constants.WHITE)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Create platforms
def create_level1():
    block_list = pygame.sprite.Group()
    #list of platform
    blocks = [[200,465],
              [350,410],
              [500,350],
              [700,290]
            ]
     
    # Loop through the list. Create the platform, add it to the list
    for item in blocks:
        block=platform.Platform(item[0],item[1])
        block_list.add(block)

    
    #list of coins
    coins = [ [80,470],
              [200,410],
              [380,355],
              [520,295],
              [720,235] ]
    
    # Loop through the list. Create coins, add it to the list
    for item in coins:
        coin= Coin(item[0],item[1])
        level1coin_list.add(coin)
    # Handle Collision
    if pygame.sprite.collide_rect(player, cube1):
        if collideCube1:
            active_sprite_list.remove(cube1)
            coin1.reveal = True
        else:
            collideCube1 = True

    if pygame.sprite.collide_rect(player, cube2):
        if collideCube2:
            active_sprite_list.remove(cube2)
            coin2.reveal = True
        else:
            collideCube2 = True
    
    level1coin_list.add(cube1)
    
    
    # list of cactus
    cactus = [ [620,485], [420,485], [40,485],[40,485] ]
     
    # Loop through the list. Create plants, add it to the list
    for item in cactus:
        cactus1= Cactus(item[0],item[1])
        level1cactus_list.add(cactus1)
     
    return block_list

def start_screen():
    screen.blit(pygame.image.load('img/bck.png'), (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
            if event.type == pygame.QUIT:
                terminate()
    

def main():
    # while True:
        coin_list = level1coin_list
        cactus_list = level1cactus_list
        block_list = create_level1()
        score = 0
        lives = 3
        level = 1
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    if event.key == pygame.K_LEFT:
                        player.changespeed_x(-6)
                        player.image = sprites[2]
                    if event.key == pygame.K_RIGHT:
                        player.changespeed_x(6)
                        player.image = sprites[1]
                    if event.key == pygame.K_SPACE:
                        player.jump(block_list)
                        player.image = sprites[3]
                    if event.key == pygame.K_DOWN:
                        player.changespeed_y(6)            
                if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_LEFT: 
                        player.changespeed_x(-0)
                    if event.key == pygame.K_RIGHT: 
                        player.changespeed_x(0)

            # Stop player around the screen if they go too far left/right
            if player.rect.x >= constants.SCREEN_WIDTH - 60:
                player.rect.x = constants.SCREEN_WIDTH - 60
        
            if player.rect.x <= 0:
                player.rect.x = 0


            coins_hit_list = pygame.sprite.spritecollide(player, coin_list, True) 

            for coin in coins_hit_list:
                # if pygame.sprite.spritecollide(coin, coins_hit_list, True):
                pygame.mixer.music.play()   
                score +=1
            
            #Plant collision
            cactus_hit_list = pygame.sprite.spritecollide(player, cactus_list, True)  
            # Check the list of plant collisions and lose lives
            for cactus in cactus_hit_list:
                lives -=1
            # Check the list of coin collisions and change score
            if lives < 0:
                break
            player.update(block_list)
            #Calculate gravity
            player.calc_grav() 
              

                 
            # Set the screen background
            screen.blit(BACKGROUND, (0,0))
            pygame.draw.rect(screen, constants.SKY, [730, 200, 50, 100],4)
            active_sprite_list.draw(screen)           
            block_list.draw(screen)
            coin_list.draw(screen)
            cactus_list.draw(screen)
            
            drawText("Level: " + str(level), font, screen, 60, 30)
            drawText("Score: " + str(score), font, screen, 720, 30)
            drawText("Lives: " + str(lives), font, screen, 720, 60)
                   
            # refresh rate   
            fpsClock.tick(FPS)
            
            # update the screen with what we've drawn. 
            pygame.display.flip()
            

        #stop the game and show game over screen
        screen.fill(constants.BLACK)
        
        drawText("GAME OVER", font, screen, (constants.SCREEN_WIDTH / 2), 300)
        drawText('Press a key to play again.', font, screen, (constants.SCREEN_WIDTH / 2), 350)
        pygame.mixer.music.stop() 
        pygame.display.update()
           
            

def terminate(): 
    pygame.quit()
    sys.exit()

start_screen()