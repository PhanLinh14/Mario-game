# import sprite
import pygame

class Goomba(pygame.sprite.Sprite):
    
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        # death bool
        self.dead = False
        self.image= pygame.image.load('img/goomba.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 540
        self.change_x= 3
    

    def move(self):
        self.rect.x += self.change_x
        if self.rect.x <= 0:
            self.change_x=3
        elif self.rect.x >= 780:
            self.change_x=-3
            

    # def die(self):
    #     # self.image = self.frames[1]
    #     # block_hit_list = pygame.sprite.spritecollide(self, blocks, False) 
 
    #     # for block in block_hit_list:
    #     self.kill()