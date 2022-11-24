import pygame
import numpy as np
from bullets import Bullet

class Tank(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill((250, 50, 0))

        self.pos_x, self.pos_y = 20, 20
        self.rect = self.image.get_rect()
        
        self.dx, self.dy = 0, 0

        self.tank_speed = 3

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
    
    def create_bullet(self):
        return Bullet(self.pos_x, self.pos_y)