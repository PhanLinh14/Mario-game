# import sprite
import pygame

class Goomba(pygame.sprite.Sprite):
    
    def __init__(self):

        # load coin sprite images
        super().__init__()

        # frame array
        self.frames = []

        # death bool
        self.dead = False

        # added: load sprite sheet
        self.sprite = pygame.image.load("img/goomba.png").convert()

        # addes: frame var for animation and timer
        self.curFrame = 0
        self.timer = 1

        # added: load images from sheet

        # add to frames
        frameCount = 0
        while frameCount < 3:
            image = sprite.get_image(self, frameCount*16, 0, 16, 16, constants.GREEN)
            self.frames.append(image)
            frameCount += 1

        # added: set starting sprite
        self.image = self.frames[0]

        # added: var for moving speed
        self.change_x = -2

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()


    # update coin 
    def update(self):
        self.move()
        self.animate()

        if self.dead == True:
            self.die()

    def move(self):
        self.rect.x += self.change_x

    def animate(self):
        # control animation speed with timer
        self.timer += 1

        if self.timer % 5 == 0:
            self.curFrame += 1

            # see if frame limit reached for either direction
            if self.curFrame == len(self.frames) - 1:
                self.curFrame = 0

            # edit image to be current frame
            self.image = self.frames[self.curFrame]

    def die(self):
        self.image = self.frames[2]
        self.change_x *= 0

        self.timer += 1

        if self.timer % 15 == 0:
            self.kill()