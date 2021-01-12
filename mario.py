import pygame, constants

class Mario(pygame.sprite.Sprite):
    change_x=0
    change_y=0
 
    # Kích hoạt nếu người chơi muốn nháy (khi nhảy jump_ready=True)
    jump_ready = False

    frame_since_collision = 0
    frame_since_jump = 0
     
    # -- Methods 
    # Constructor function 
    def __init__(self,x,y): 
        # Gọi hàm dựng của cha
        pygame.sprite.Sprite.__init__(self) 
           
        # cài đặt hình ảnh của mario
        self.image = pygame.image.load("img/mario.png")
        
        # điểm trên cùng bên trái được đặt là điểm bắt đâu
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
       
    # Thay đổi tốc độ( thay đổi tọa độ) của người chơi 
    def go_left(self):
        self.change_x = -6
 
    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0
 
    def changespeed_y(self,y):
        self.change_y = y
           
    # Vị trí mới
    def update(self,blocks): 
 
        # Gán vị trí cũ =old, sau đó vị trí mới = cũ + độ thay đổi tọa độ
        old_x = self.rect.x
        self.rect.x = old_x + self.change_x
 
        collide = pygame.sprite.spritecollide (self, blocks, False)
        if collide:
            # khi người chơi va chạm với vật thể (vật thể ko gây sát thương) thì quay lại vị trí hiện tại
            self.rect.x = old_x
 
        # Gán vị trí cũ =old, sau đó vị trí mới = cũ + độ thay đổi tọa độ
        old_y = self.rect.y 
        self.rect.y = old_y + self.change_y 
         
        block_hit_list = pygame.sprite.spritecollide(self, blocks, False) 
 
        for block in block_hit_list:
            #khi người chơi va chạm với vật thể ( vật thể  gây sát thương ấy) thì quay về vị trí hiện tại
            self.rect.y = old_y
            self.rect.x = old_x
 
            # Stop player vertical movement
            self.change_y = 0
 
            # Start counting frames since player hit something
            self.frame_since_collision = 0
        
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
 
    # Hàm nhảy
    def jump(self, blocks):
        self.jump_ready = True
        self.frame_since_jump=0
        




