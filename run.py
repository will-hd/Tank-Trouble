import pygame
import numpy as np
from tank import Tank
from bullets import Bullet
import constants
import wall
import random

# Initialise pygame 
pygame.init()
font = pygame.font.SysFont('Arial', 30)


class Game():
    def __init__(self, DISPLAY_WIDTH, DISPLAY_HEIGHT) -> None:
        self.clock = pygame.time.Clock()

        self.display_width, self.display_height = DISPLAY_WIDTH, DISPLAY_HEIGHT
        
        # Create screen
        self.screen = pygame.display.set_mode((self.display_width, self.display_height))
        self.backdrop = pygame.Surface([self.display_width, self.display_height])
        self.backdrop.fill(constants.WHITE)
        self.backdrop_box = self.screen.get_rect()

        # Sprite groups
        self.tank_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.all_bullet_group = pygame.sprite.Group()
        
        self.create_map()
        self.create_tanks()
        self.create_score_display()

    def create_tanks(self):
        self.tanks = [
            Tank(game=self, PLAYER_ID=0, 
            init_position=self.TANK_INIT_POSITIONS[0], init_angle=random.randrange(0, 360)), 
            Tank(game=self, PLAYER_ID=1, 
            init_position=self.TANK_INIT_POSITIONS[1], init_angle=random.randrange(0, 360))
            ]
        self.tanks_score = [0, 0]
        self.tanks_alive = [True, True]

    def reset(self):
        """
        Removes all bullets, sets all tanks alive and gives them a new starting
        position from the list of possible starting positions for the map.
        """
        pygame.time.delay(1000)

        self.all_bullet_group.empty()
        starting_pos = random.sample(self.TANK_INIT_POSITIONS, 2)

        for tank in self.tanks:
            tank.tanks_bullet_group.empty()
            if not tank.IS_ALIVE:
                self.tank_group.add(tank)
                tank.IS_ALIVE = True
            tank.position = pygame.math.Vector2(starting_pos[tank.PLAYER_ID])

    def run(self):
        # Game loop
        
        GAME_RUNNING = True

        while GAME_RUNNING:
            self.dt = self.clock.tick(60) / 1000 # Using dt method makes speed FPS invariant

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GAME_RUNNING = False

            keys = pygame.key.get_pressed()
            

            # Draw screen and grid
            self.screen.blit(self.backdrop, self.backdrop_box)
            self.wall_group.draw(self.screen)

            
            self.all_bullet_group.update()
            self.all_bullet_group.draw(self.screen)


            self.tank_group.update(keys)
            self.tank_group.draw(self.screen)
            
            self.display_score()

            self.tanks_alive = [tank.IS_ALIVE for tank in self.tanks]

            if False in self.tanks_alive:
                dscore = [int(x == True) for x in self.tanks_alive]
                self.tanks_score = [sum(pair) for pair in zip(self.tanks_score, dscore)]
                self.reset()

            ###### Uncomment if wanting to see rect "hitboxes" ######
            # for tank in self.tank_group:
            #     pygame.draw.rect(self.screen, (0, 0, 0), (*tank.rect.topleft, *tank.image.get_size()), 1)
            
            # for bullet in self.all_bullet_group:
            #     pygame.draw.rect(self.screen, (0, 0, 0), (*bullet.rect.topleft, *bullet.image.get_size()), 1)

            pygame.display.flip()

    def create_score_display(self):
        """
        Creates tank drawings for use in scoreboard.
        """
        self.scoreboard_tank1 = pygame.Surface([30, 40], pygame.SRCALPHA)
        pygame.draw.rect(self.scoreboard_tank1, constants.TANK_COLORS[0][0], (0, 10, 30, 30))
        pygame.draw.rect(self.scoreboard_tank1, constants.TANK_COLORS[0][1], (10, 10, 10, 20))
        pygame.draw.rect(self.scoreboard_tank1, constants.TANK_COLORS[0][2], (12, 0, 6, 25))
        self.scoreboard_tank2 = pygame.Surface([30, 40], pygame.SRCALPHA)
        pygame.draw.rect(self.scoreboard_tank2, constants.TANK_COLORS[1][0], (0, 10, 30, 30))
        pygame.draw.rect(self.scoreboard_tank2, constants.TANK_COLORS[1][1], (10, 10, 10, 20))
        pygame.draw.rect(self.scoreboard_tank2, constants.TANK_COLORS[1][2], (12, 0, 6, 25))
        
    def display_score(self):
        score1 = font.render(f"{self.tanks_score[0]}", 1, constants.BLACK)
        score2 = font.render(f"{self.tanks_score[1]}", 1, constants.BLACK)
        self.screen.blit(score1, (240, 825))
        self.screen.blit(score2, (540, 825))
        self.screen.blit(self.scoreboard_tank1, (200, 820))
        self.screen.blit(self.scoreboard_tank2, (500, 820))

    def create_map(self):
        self.TANK_INIT_POSITIONS = []
        for row, tiles in enumerate(wall.wall_map):
            for col, tile in enumerate(tiles):
                if tile == 1:
                    wall.Wall(self.wall_group, col, row)
                if tile == 2:
                    self.TANK_INIT_POSITIONS.append((col*constants.BLOCKSIZE, row*constants.BLOCKSIZE))

    def end_screen(self):
        END_RUNNING = True

        while END_RUNNING:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    END_RUNNING = False
            
            font = pygame.font.SysFont('arial', 80)
            score = font.render(f'Winner' )


if __name__ == '__main__':
    g = Game(
        DISPLAY_WIDTH=constants.DISPLAY_WIDTH,
        DISPLAY_HEIGHT=constants.DISPLAY_HEIGHT
        )
    
    g.run()

