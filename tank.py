import pygame
import numpy as np
from bullets import Bullet
import constants

vector = pygame.math.Vector2

class Tank(pygame.sprite.Sprite):
    def __init__(self, game, PLAYER_ID) -> None:
        self.game = game
        self.PLAYER_ID = PLAYER_ID
        super().__init__(self.game.tank_group)
        self.tanks_bullet_group = pygame.sprite.Group()

        self.position = vector(constants.DISPLAY_WIDTH/2, constants.DISPLAY_HEIGHT/2)
        self.init_image()

        self.dpos = vector(0, 0)
        self.angle = 0
        self.direction = vector(1, 0)
        self.rotation_offset = 0

        self.tank_speed = 4
        self.shoot_frequency: int = 300 #/milliseconds
        self.bullet_ready: bool = True
        self.max_bullets = 5

        self.previous_time = pygame.time.get_ticks()
    
    def init_image(self):
        """
        Create tank image and center at position. Store original image for use
        in rotations
        """
        self.image = pygame.Surface([40, 30], pygame.SRCALPHA)
        # Tank body
        pygame.draw.rect(self.image, constants.TANK_COLORS[self.PLAYER_ID][0], (0, 0, 30, 30))
        # Tank turret
        pygame.draw.rect(self.image, constants.TANK_COLORS[self.PLAYER_ID][1], (10, 10, 20, 10))
        # Tank barrel
        pygame.draw.rect(self.image, constants.TANK_COLORS[self.PLAYER_ID][2], (15, 12, 25, 6))
        
        self.mask = pygame.mask.from_surface(self.image)

        self.original_image = self.image.copy()
        self.original_center = self.original_image.get_rect().center
        
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        

    def update(self, keys):
        """
        Update tank's position
        """
        self.position_before_collide = self.position.copy()
        self.angle_before_collide = self.angle

        self.handle_key_press(keys)

        self.direction = vector(1, 0).rotate(-self.angle)
        self.image, self.rect, self.mask = self.rotate_image()

        # Update position
        self.position += self.dpos # floating point accuracy
        self.rect.center = self.position # integer
        
        # Check if rect collides, then check if mask collides. Hence, we are only
        # checking mask (intesive) if sprite is already close to walls
        if pygame.sprite.spritecollide(self, self.game.wall_group, False, pygame.sprite.collide_rect):
            if pygame.sprite.spritecollide(self, self.game.wall_group, False, pygame.sprite.collide_mask):
                # Reset sprite to state before collision
                self.angle = self.angle_before_collide
                self.direction = vector(1, 0).rotate(-self.angle)
                self.image, self.rect, self.mask = self.rotate_image()

                self.position = self.position_before_collide.copy()
                self.rect.center = self.position
        
        
        self.dpos = vector(0, 0) # Reset back to zero for next frame

    
    def rotate_image(self):
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        new_rect = rotated_image.get_rect()
        new_mask = pygame.mask.from_surface(rotated_image)

        return rotated_image, new_rect, new_mask

    def control(self, forward):
        self.dpos += self.direction * self.tank_speed * forward

    def handle_key_press(self, keys):

        if keys[constants.MOVEMENT_KEYS[self.PLAYER_ID]['CLOCKWISE']]:
                self.angle -= 6
        if keys[constants.MOVEMENT_KEYS[self.PLAYER_ID]['ANTI-CLOCKWISE']]:
                self.angle += 6
        if keys[constants.MOVEMENT_KEYS[self.PLAYER_ID]['FORWARD']]:
                self.control(forward=+1)
        if keys[constants.MOVEMENT_KEYS[self.PLAYER_ID]['BACKWARD']]:
                self.control(forward=-1)

        # Shoot bullet
        if keys[constants.MOVEMENT_KEYS[self.PLAYER_ID]['SHOOT']]:
            if self.can_shoot():
                self.create_bullet()

    def can_shoot(self) -> bool:
        """
        Returns whether the tank is able to shoot given time spacing between last 
        shot.
        """
        current_time = pygame.time.get_ticks()
        interval = current_time - self.previous_time
       
        if interval >= self.shoot_frequency and len(self.tanks_bullet_group) < self.max_bullets:
            self.previous_time = current_time
            return True
        else:
            return False

    def create_bullet(self):
        Bullet(self.position, self.game, self.tanks_bullet_group, direction=self.direction)