import pygame
import constants


class Bullet(pygame.sprite.Sprite):
    def __init__(self, 
                position, 
                game,
                tanks_bullet_group,
                direction) -> None:
        self.game = game
        super().__init__(self.game.all_bullet_group, tanks_bullet_group)

        # Surface, image, rect
        self.image = pygame.Surface([8, 8], pygame.SRCALPHA)
        # self.image.fill((0, 0, 0))
        # self.image.set_colorkey((0, 0, 0))
        # pygame.draw.rect(self.image, (0,0,0), (0, 0, 25, 6))
        pygame.draw.circle(self.image, constants.BULLET_COLOR, (4, 4), radius=4)
        self.mask = pygame.mask.from_surface(self.image)

        self.direction = direction
        self.position = position.copy() + self.direction*20 # Bullet spawned closer to end of barrel
        self.rect = self.image.get_rect(center=self.position)
        

        self.bullet_speed = 200
        self.lifetime = 8000 # milliseconds
        self.spawn_time = pygame.time.get_ticks()
        
        self.frame = 0

    def update(self):
        """
        Move the bullet.
        Move in x direction first, check collision, then do y.
        e.g. see https://www.youtube.com/watch?v=vAfveKX1pSc
        and https://www.reddit.com/r/pygame/comments/7bxo9r/checking_which_side_a_sprite_collides_with_another/
        """

        # Store previous state before collision, to reuse if next move causes collison
        self.position_before_collision = self.position.copy()
        self.positionx_before_collision = self.position_before_collision.x
        self.positiony_before_collision = self.position_before_collision.y

        self.position += self.direction * self.bullet_speed * self.game.dt

        # Check if new movement has caused collision along x
        self.rect.centerx = self.position.x
        if pygame.sprite.spritecollide(self, self.game.wall_group, False):
            self.direction.x *= -1
            self.position = self.position_before_collision
            self.rect.center = self.position
        
        # Now check if new movement has caused collision along y
        self.rect.centery = self.position.y
        if pygame.sprite.spritecollide(self, self.game.wall_group, False):
            self.direction.y *= -1
            self.position = self.position_before_collision
            self.rect.center = self.position

        
        current_time = pygame.time.get_ticks()

        # Check if bullet collides with any tanks
        # Allow delay time so that bullet can leave the tank's rect.
        # Then check if rects collide before mask for better efficiency
        if current_time - self.spawn_time >= 50:
            if pygame.sprite.spritecollide(self, self.game.tank_group, False, pygame.sprite.collide_rect):
                # Now check if bullet collides with tank's mask
                tank_hit_list = pygame.sprite.spritecollide(self, self.game.tank_group, True, pygame.sprite.collide_mask)
                # maybe add offset so that bullet has to overlap slightly?
                
                if tank_hit_list:
                    self.kill() # Kill bullet as well as tank
                    for tank in tank_hit_list: # do we really need to iterate over list?
                        tank.IS_ALIVE = False
                
        # Bullet has finite lifetime
        if current_time - self.spawn_time >= self.lifetime:
            self.kill()

    def draw(self):
        pygame.draw.circle(self.image, (64, 64, 62), self.rect.center, 5)