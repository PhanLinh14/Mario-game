import pygame

class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite. __init__(self)

        self.image = pygame.image.load("img/cube.png")
        # Make top-left corner the passed-in location. 
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y