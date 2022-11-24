import pygame
import constants


class Bullet(pygame.sprite.Sprite):
    def __init__(self, 
                position, 
                bullet_group, 
                wall_group,
                direction) -> None:
        super().__init__(bullet_group)

        # Surface, image, rect
        self.image = pygame.Surface([8, 8])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, constants.BULLET_COLOR, (4, 4), radius=4)
        # self.image = pygame.image.load("bullet.png")

        self.position = position.copy()
        self.rect = self.image.get_rect(center=self.position)

        self.bullet_speed = 8
        self.direction = direction

        self.walls = wall_group

    def update(self):
        """
        Move the bullet
        """
        if pygame.sprite.spritecollide(self, self.walls, False, False):
            self.direction *= -1
            self.position += self.direction * self.bullet_speed
        else:
            self.position += self.direction * self.bullet_speed
        self.rect.center = self.position

        if self.rect.x >= constants.DISPLAY_WIDTH-10:
            self.kill()

    def draw(self):
        pygame.draw.circle(self.image, (64, 64, 62), self.rect.center, 5)