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

        self.direction = direction
        self.position = position.copy() + self.direction*6
        self.rect = self.image.get_rect(center=self.position)
        

        self.bullet_speed = 5
        self.lifetime = 8000 # milliseconds
        self.spawn_time = pygame.time.get_ticks()
        
        self.walls = wall_group
        self.frame = 0

    def update(self):
        """
        Move the bullet.
        Move in x direction first, check collision, then do y.
        e.g. see https://www.youtube.com/watch?v=vAfveKX1pSc
        and https://www.reddit.com/r/pygame/comments/7bxo9r/checking_which_side_a_sprite_collides_with_another/
        """
        self.position_before_collision = self.position.copy()
        self.positionx_before_collision = self.position_before_collision.x
        self.positiony_before_collision = self.position_before_collision.y

        self.position += self.direction * self.bullet_speed

        # Do x
        self.rect.centerx = self.position.x
        if pygame.sprite.spritecollide(self, self.walls, False):
            self.direction.x *= -1
            self.position = self.position_before_collision
            self.rect.center = self.position
        
        # Do y
        self.rect.centery = self.position.y
        if pygame.sprite.spritecollide(self, self.walls, False):
            self.direction.y *= -1
            print(self.direction)
            self.position = self.position_before_collision
            self.rect.center = self.position
            
        if pygame.time.get_ticks() - self.spawn_time >= self.lifetime:
            self.kill()

    def draw(self):
        pygame.draw.circle(self.image, (64, 64, 62), self.rect.center, 5)