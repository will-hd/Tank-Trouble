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
        self.direction = direction

        self.bullet_speed = 6
        self.lifetime = 8000 # milliseconds
        self.spawn_time = pygame.time.get_ticks()
        
        self.walls = wall_group

    def update(self):
        """
        Move the bullet
        """
        if pygame.sprite.spritecollide(self, self.walls, False):
            if self.direction.y > 0 and self.direction.x == 0:
                self.direction *= -1
            elif self.direction.y < 0 and self.direction.x == 0:
                self.direction *= -1
            elif self.direction.x > 0 and self.direction.y == 0:
                self.direction *= -1
            elif self.direction.x < 0 and self.direction.y == 0:
                self.direction *= -1
            elif self.direction.x > 0 and self.direction.y < 0:
                self.direction.x = -self.direction.x
            elif self.direction.x < 0 and self.direction.y < 0:
                self.direction.y = -self.direction.y
            elif self.direction.x < 0 and self.direction.y > 0:
                self.direction.x = -self.direction.x
            elif self.direction.x > 0 and self.direction.y > 0:
                self.direction.y = -self.direction.y
            self.position += self.direction * self.bullet_speed

        else:
            self.position += self.direction * self.bullet_speed
        self.rect.center = self.position

        if pygame.time.get_ticks() - self.spawn_time >= self.lifetime:
            self.kill()

    def draw(self):
        pygame.draw.circle(self.image, (64, 64, 62), self.rect.center, 5)