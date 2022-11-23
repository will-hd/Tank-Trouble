import pygame
import numpy as np

class Tank(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([30, 30])
        self.image.fill((250, 50, 0))

        self.rect = self.image.get_rect()

        self.X, self.Y = 200, 200
        self.dx, self.dy = 0, 0
        self.rect.x, self.rect.y = self.X, self.Y 

    def control(self, dx, dy):
        self.dx += dx
        self.dy += dy

    def update(self):
        """
        Update tank's position
        """
        # Update with floating point accuracy
        self.X += self.dx
        self.Y += self.dy

        # Conver to integer
        self.rect.x = int(self.X)
        self.rect.y = int(self.Y)

        (self.dx, self.dy) = (0, 0) # Reset back to zero for next frame