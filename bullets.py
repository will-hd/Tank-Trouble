import pygame
import constants

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x: float, pos_y: float, bullet_group) -> None:
        super().__init__(bullet_group)

        self.image = pygame.Surface([8, 8])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, constants.BULLET_COLOR, (4, 4), radius=4)
        # self.image = pygame.image.load("bullet.png")

        self.rect = self.image.get_rect(center = (int(pos_x), int(pos_y)))

    def update(self):
        self.rect.x += 5
        
        if self.rect.x >= constants.DISPLAY_WIDTH-100:
            self.kill()

    def draw(self):
        pygame.draw.circle(self.image, (64, 64, 62), self.rect.center, 5)