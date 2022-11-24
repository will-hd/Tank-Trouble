import pygame
import numpy as np
from bullets import Bullet

vector = pygame.math.Vector2

class Tank(pygame.sprite.Sprite):
    def __init__(self, tank_group, wall_group) -> None:
        super().__init__(tank_group)

        self.image = pygame.Surface([60, 40], pygame.SRCALPHA)
        pygame.draw.rect(self.image, (0, 96, 0), (0, 00, 50, 40))
        pygame.draw.rect(self.image, (0, 128, 0), (10, 10, 30, 20))
        pygame.draw.rect(self.image, (32, 32, 96), (20, 16, 40, 8))

        self.position = vector(20, 20)
        self.rect = self.image.get_rect()
        
        self.dpos = vector(0, 0)

        self.tank_speed = 5.11

        self.shoot_frequency: int = 300 #/milliseconds
        self.bullet_ready: bool = True

        self.last_time = pygame.time.get_ticks()

        self.bullet_group = pygame.sprite.Group() # Bullet group for each tank
        self.wall_group = wall_group

    def control(self, dx, dy):
        self.dpos += vector(dx, dy)

    def update(self):
        """
        Update tank's position
        """
        self.position += self.dpos #floating point
        self.rect.center = self.position # integer
        print(self.position, self.rect.center)
    
        self.dpos = vector(0, 0) # Reset back to zero for next frame
    
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
        Bullet(self.position, self.bullet_group, self.wall_group, direction=vector(1,0))