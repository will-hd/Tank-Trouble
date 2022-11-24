import pygame
import numpy as np
from tank import Tank
from bullets import Bullet

# Initialise pygame 
pygame.init()

class Game():
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()

        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 1200, 800
        
        # Create screen
        self.screen = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.backdrop = pygame.Surface([self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT])
        self.backdrop_box = self.screen.get_rect()

        self.add_tank()
        self.bullet_group = pygame.sprite.Group()
    
    def add_tank(self) -> None:
        # Instantiate a tank and sprite group
        self.tank = Tank()
        self.tank_group = pygame.sprite.Group()
        self.tank_group.add(self.tank)

    def run(self):
        # Game loop

        GAME_RUNNING = True

        while GAME_RUNNING:

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

            if keys[pygame.K_f]:
                self.bullet_group.add(self.tank.create_bullet())

            # Draw screen and grid
            self.screen.blit(self.backdrop, self.backdrop_box)
            self.draw_grid()

            self.bullet_group.update()
            self.tank_group.update()
            self.bullet_group.draw(self.screen)
            self.tank_group.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)

    def draw_grid(self):

        BLOCKSIZE = 50 #Set the size of the grid block

        for x in range(0, self.DISPLAY_WIDTH, BLOCKSIZE):
            for y in range(0, self.DISPLAY_HEIGHT, BLOCKSIZE):

                rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)

if __name__ == '__main__':
    g = Game()
    g.run()

