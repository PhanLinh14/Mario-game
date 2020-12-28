import pygame

class Mario(pygame.sprite.Sprite):
    change_x=0
    change_y=0
 
    # Triggered if the player wants to jump.
    jump_ready = False
 
    # Count of frames since the player hit 'jump' and we
    # collided against something. Used to prevent jumping
    # when we haven't hit anything.
    frame_since_collision = 0
    frame_since_jump = 0
     
    # -- Methods 
    # Constructor function 
    def __init__(self,x,y): 
        # Call the parent's constructor 
        pygame.sprite.Sprite.__init__(self) 
           
        # Set height, width 
        self.image = pygame.image.load("img/mario.png")
        
        # Make top-left corner the passed-in location. 
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
       
    # Change the speed of the player 
    def changespeed_x(self,x):
        self.change_x = x
 
    def changespeed_y(self,y):
        self.change_y = y
           
    # Find a new position for the player 
    def update(self,blocks): 
 
        # Save the old x position, update, and see if player collided.
        old_x = self.rect.x
        new_x = old_x + self.change_x
        self.rect.x = new_x
 
        collide = pygame.sprite.spritecollide (self, blocks, False)
        if collide:
            # Player collided, go back to the old pre-collision location
            self.rect.x = old_x
 
        # Save the old y position, update, and see if we collided.
        old_y = self.rect.y 
        new_y = old_y + self.change_y 
        self.rect.y = new_y
         
        block_hit_list = pygame.sprite.spritecollide(self, blocks, False) 
 
        for block in block_hit_list:
            # Player collided. Set the old pre-collision location.
            self.rect.y = old_y
            self.rect.x = old_x
 
            # Stop player vertical movement
            self.change_y = 0
 
            # Start counting frames since player hit something
            self.frame_since_collision = 0
 
        # If the player recently asked to jump, and have recently
        # had ground under his feet, go ahead and change the velocity
        # to send player upwards
        if self.frame_since_collision < 6 and self.frame_since_jump < 6:
            self.frame_since_jump = 100
            self.change_y -= 9
 
        # Increment frame counters
        self.frame_since_collision+=1
        self.frame_since_jump+=1
 
    # Calculate effect of gravity.
    def calc_grav(self):
        self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= 500 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 500
            self.frame_since_collision = 0
 
    # Called when user hits 'jump' button
    def jump(self,blocks):
        self.jump_ready = True
        self.frame_since_jump = 0
         
pygame.init() 



