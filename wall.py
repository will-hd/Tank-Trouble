import pygame
import constants
import numpy as np

wall_map = np.loadtxt("maps\map1.txt", dtype="int8")

class Wall(pygame.sprite.Sprite):   
    def __init__(self, wall_group, col, row) -> None:
        super().__init__(wall_group)

        self.image = pygame.Surface([constants.BLOCKSIZE, constants.BLOCKSIZE])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y  = col*constants.BLOCKSIZE, row*constants.BLOCKSIZE

