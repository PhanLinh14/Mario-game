import pygame
# Platform sprite
class Platform (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/brickwall.png')
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y