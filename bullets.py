import pygame
import constants

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x: float, pos_y: float) -> None:
        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill((0, 250, 0))

        self.rect = self.image.get_rect(center = (int(pos_x), int(pos_y)))

    def update(self):
        self.rect.x += 1
        
        if self.rect.x >= constants.DISPLAY_WIDTH:
            self.kill()
