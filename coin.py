import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite. __init__(self)
        pygame.mixer.music.load('sounds/Pickup.wav')
        self.image = pygame.image.load("img/coin.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        # Make top-left corner the passed-in location. 
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
      