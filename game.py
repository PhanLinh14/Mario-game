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

coin1 = Coin(200, 300)
coin2 = Coin(450, 270)
active_sprite_list.add(player)

level1coin_list = pygame.sprite.Group()
level1cactus_list = pygame.sprite.Group()
level2coin_list = pygame.sprite.Group()
level2cactus_list = pygame.sprite.Group()

#Draw text function           
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, constants.WHITE)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def terminate():
    pygame.mixer.quit() 
    pygame.quit()
    sys.exit()

# Create platforms
def create_level1():
    block_list = pygame.sprite.Group()
    #list of platform
    blocks = [[200,465],
              [350,410],
              [500,350],
              [720,290]]
     
    # Loop through the list. Create the platform, add it to the list
    for item in blocks:
        block=platform.Platform(item[0],item[1])
        block_list.add(block)
    cubes =[[200, 300],[470, 200]]
    for item in cubes:
        cube=Cube(item[0],item[1])
        block_list.add(cube)
    
    #list of coins
    coins = [ [75,390],[90,390],[240, 400], [380,340], [520,290],[680,235] ]
    
    # Loop through the list. Create coins, add it to the list
    for item in coins:
        coin= Coin(item[0],item[1])
        level1coin_list.add(coin)
    
    # list of cactus
    cactus = [ [620,485], [650,485],[430,485], [310,485] ]
     
    # Loop through the list. Create plants, add it to the list
    for item in cactus:
        cactus1= Cactus(item[0],item[1])
        level1cactus_list.add(cactus1)
     
    return block_list

# Create platforms
def create_level2():
    block_list = pygame.sprite.Group()
    #list of platform
    blocks = [[40,370],
              [200,465],
              [230,290],
              [370,200],
              [500,350],
              [720,290]]
     
    # Loop through the list. Create the platform, add it to the list
    for item in blocks:
        block=platform.Platform(item[0],item[1])
        block_list.add(block)
    cubes =[[200, 140],[420, 50]]
    for item in cubes:
        cube=Cube(item[0],item[1])
        block_list.add(cube)
    
    #list of coins
    coins = [ [215, 420],[95,240],[110,240],[255,220],[350,100],[530,280],[680,220] ]
    
    # Loop through the list. Create coins, add it to the list
    for item in coins:
        coin= Coin(item[0],item[1])
        level2coin_list.add(coin)
    
    # list of cactus
    cactus2 = [ [660,485],[620,485],[430,485],[330,485] ]
     
    # Loop through the list. Create plants, add it to the list
    for item in cactus2:
        cactus= Cactus(item[0],item[1])
        level2cactus_list.add(cactus)
     
    return block_list

def start_screen():  
    image_start = pygame.image.load('img/start_btn1.png')
    image_exit = pygame.image.load('img/exit_btn1.png')
    continues = True
    while continues:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                if 160 < event.pos[0] < 400 and 150 < event.pos[1] < 520:
                    image_start = pygame.image.load('img/start_btn2.png')
                else:
                    image_start = pygame.image.load('img/start_btn1.png')
                    
                if 480 < event.pos[0] < 600 and 350 < event.pos[1] < 520:
                    image_exit = pygame.image.load('img/exit_btn2.png')
                else:
                    image_exit = pygame.image.load('img/exit_btn1.png')
            #checks if a mouse is clicked 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 160 < event.pos[0] < 400 and 150 < event.pos[1] < 520:
                    pygame.mixer.stop()
                    continues = False
                if 480 < event.pos[0] < 600 and 350 < event.pos[1] < 520:
                    terminate()
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(pygame.image.load('img/bck.png'), (0, 0))
        screen.blit(image_start, (160, 480))
        screen.blit(image_exit, (480, 480))
        pygame.display.flip()
    main()

def main():
    # while True:
        coin_list = level1coin_list
        cactus_list = level1cactus_list
        block_list = create_level1()
        score = 0
        lives = 3
        level = 1
        pygame.mixer.Sound('sounds/mario_theme.ogg').play(-1)
        gameover= False
        gameloop= True
        while gameloop:
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
            if lives <= 0:
                gameover= True
                gameloop= False
                
            player.update(block_list)
            if 740 > player.rect.x > 730 and 290 > player.rect.y > 205:
                if level == 1:
                    block_list = create_level2()
                    coin_list = level2coin_list
                    cactus_list = level2cactus_list
                    level = 2
                    player.rect.x = 0
                    player.rect.y = 500
            
                elif level == 2:
                    break
            #Calculate gravity
            player.calc_grav() 
                             
            # Set the screen background
            screen.blit(BACKGROUND, (0,0))
            screen.blit(pygame.image.load('img/door.png'), (740,205))
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
            
        pygame.mixer.music.stop()
        if gameover:
            game_over()   
           
            


def game_over():
    
    pygame.mixer.stop()
    continues= True
    while continues:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                continues= False
                
     #stop the game and show game over screen
        screen.fill(constants.BLACK)      
        drawText("GAME OVER", font, screen, (constants.SCREEN_WIDTH / 2), 300)
        drawText('Press a key to play again.', font, screen, (constants.SCREEN_WIDTH / 2), 350)
        pygame.display.flip()
    main()
start_screen()