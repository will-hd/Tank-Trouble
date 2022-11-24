import pygame
import numpy as np
from bullets import Bullet

class Tank(pygame.sprite.Sprite):
    def __init__(self, tank_group) -> None:
        super().__init__(tank_group)

        self.image = pygame.Surface([60, 40], pygame.SRCALPHA)
        pygame.draw.rect(self.image, (0, 96, 0), (0, 00, 50, 40))
        pygame.draw.rect(self.image, (0, 128, 0), (10, 10, 30, 20))
        pygame.draw.rect(self.image, (32, 32, 96), (20, 16, 40, 8))


        self.pos_x, self.pos_y = 20, 20
        self.rect = self.image.get_rect()
        
        self.dx, self.dy = 0, 0

        self.tank_speed = 5

        self.shoot_frequency: int = 300 #/milliseconds
        self.bullet_ready: bool = True

        self.last_time = pygame.time.get_ticks()

        self.bullet_group = pygame.sprite.Group() # Bullet group for each tank

    def control(self, dx, dy):
        self.dx += dx
        self.dy += dy

    def update(self):
        """
        Update tank's position
        """
        # Update with floating point accuracy
        self.pos_x += self.dx
        self.pos_y += self.dy

        # Convert to integer for pygame to use
        self.rect.centerx = int(self.pos_x)
        self.rect.centery = int(self.pos_y)

        (self.dx, self.dy) = (0, 0) # Reset back to zero for next frame
    
    def can_shoot(self) -> bool:
        """
        returns whether the tank is able to shoot given time spacing between last 
        shot.
        """
        current_time = pygame.time.get_ticks()
        interval = current_time - self.last_time
        
        if interval >= self.shoot_frequency:
            self.last_time = current_time
            return True
        else:
            return False


    def create_bullet(self):
        Bullet(self.pos_x, self.pos_y, self.bullet_group)