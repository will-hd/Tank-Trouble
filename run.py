import pygame
import numpy as np
from tank import Tank
from bullets import Bullet
import constants
import wall

# Initialise pygame 
pygame.init()

class Game():
    def __init__(self, DISPLAY_WIDTH, DISPLAY_HEIGHT) -> None:
        self.clock = pygame.time.Clock()

        self.display_width, self.display_height = DISPLAY_WIDTH, DISPLAY_HEIGHT
        
        # Create screen
        self.screen = pygame.display.set_mode((self.display_width, self.display_height))
        self.backdrop = pygame.Surface([self.display_width, self.display_height])
        self.backdrop.fill(constants.WHITE)
        self.backdrop_box = self.screen.get_rect()

        self.tank_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        
        self.new_map()

        self.tank = Tank(self.tank_group)


    def run(self):
        # Game loop

        GAME_RUNNING = True

        while GAME_RUNNING:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GAME_RUNNING = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.tank.control(self.tank.tank_speed, 0)
            if keys[pygame.K_LEFT]:
                self.tank.control(-self.tank.tank_speed, 0)
            if keys[pygame.K_UP]:
                self.tank.control(0, -self.tank.tank_speed)
            if keys[pygame.K_DOWN]:
                self.tank.control(0, +self.tank.tank_speed)
            # Shoot bullet
            # if keys[pygame.K_f]:
            #     if self.tank.can_shoot():
            #         self.bullet_group.add(self.tank.create_bullet())
            if keys[pygame.K_f]:
                if self.tank.can_shoot():
                    self.tank.create_bullet()

            # Draw screen and grid
            self.screen.blit(self.backdrop, self.backdrop_box)
            self.wall_group.draw(self.screen)

            for tank in self.tank_group:
                self.tank.bullet_group.update()
                self.tank.bullet_group.draw(self.screen)

            self.tank_group.update()
            self.tank_group.draw(self.screen)

            pygame.display.flip()
            
    def new_map(self):
        BLOCKSIZE = 20 #Set the size of the grid block

        for row, tiles in enumerate(wall.wall_map):
            for col, tile in enumerate(tiles):
                if tile == 1:
                    wall.Wall(self.wall_group, col, row)


if __name__ == '__main__':
    g = Game(
        DISPLAY_WIDTH=constants.DISPLAY_WIDTH,
        DISPLAY_HEIGHT=constants.DISPLAY_HEIGHT
        )
    
    g.run()

