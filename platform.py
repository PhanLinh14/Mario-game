import pygame
# Platform sprite
class Platform (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/brickwall.png')   
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed= 1
        self.old_x = x
        self.old_y = y

    def move_x(self,x2):
        self.rect.x += self.speed
        if self.rect.x <= self.old_x:
                self.speed=1
        elif self.rect.x >= x2:
                self.speed=-1

    # def move_y(self,y2):
    #     self.rect.y -= self.speed
    #     if self.rect.y >= self.old_y:
    #             self.speed=-1
    #     elif self.rect.y <= y2:
    #             self.speed=1