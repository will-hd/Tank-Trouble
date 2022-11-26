import pygame
import numpy as np
from tank import Tank
from bullets import Bullet
import constants
import wall

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

        self.tank_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.all_bullet_group = pygame.sprite.Group()
        
        self.create_map()

        self.tanks = [Tank(game=self, PLAYER_ID=0), Tank(game=self, PLAYER_ID=1)]
        # self.tank1 = Tank(game=self, PLAYER_ID=0)
        # self.tank2 = Tank(game=self, PLAYER_ID=1)
        self.tanks_score = [0, 0]
        self.tanks_alive = [True, True]

        self.setup_score_display()

    def reset(self):
        pygame.time.delay(1000)
        self.all_bullet_group.empty()
        for tank in self.tanks:
            tank.tanks_bullet_group.empty()
            if not tank.IS_ALIVE:
                self.tank_group.add(tank)
                tank.IS_ALIVE = True
            tank.position = pygame.math.Vector2(constants.TANK_INIT_POSITIONS[tank.PLAYER_ID])

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
                print("someone died!!")
                dscore = [int(x == True) for x in self.tanks_alive]
                self.tanks_score = [sum(pair) for pair in zip(self.tanks_score, dscore)]
                print(self.tanks_score)
                self.reset()

            # for tank in self.tank_group:
            #     pygame.draw.rect(self.screen, (0, 0, 0), (*tank.rect.topleft, *tank.image.get_size()), 1)
            
            # for bullet in self.all_bullet_group:
            #     pygame.draw.rect(self.screen, (0, 0, 0), (*bullet.rect.topleft, *bullet.image.get_size()), 1)

            pygame.display.flip()
        

    def setup_score_display(self):
        self.score_tank1 = pygame.Surface([30, 40], pygame.SRCALPHA)
        pygame.draw.rect(self.score_tank1, constants.TANK_COLORS[0][0], (0, 10, 30, 30))
        pygame.draw.rect(self.score_tank1, constants.TANK_COLORS[0][1], (10, 10, 10, 20))
        pygame.draw.rect(self.score_tank1, constants.TANK_COLORS[0][2], (12, 0, 6, 25))
        

        self.score_tank2 = pygame.Surface([30, 40], pygame.SRCALPHA)
        pygame.draw.rect(self.score_tank2, constants.TANK_COLORS[1][0], (0, 10, 30, 30))
        pygame.draw.rect(self.score_tank2, constants.TANK_COLORS[1][1], (10, 10, 10, 20))
        pygame.draw.rect(self.score_tank2, constants.TANK_COLORS[1][2], (12, 0, 6, 25))
        


    def display_score(self):
        score1 = font.render(f"{self.tanks_score[0]}", 1, constants.BLACK)
        score2 = font.render(f"{self.tanks_score[1]}", 1, constants.BLACK)
        self.screen.blit(score1, (240, 825))
        self.screen.blit(score2, (540, 825))
        self.screen.blit(self.score_tank1, (200, 820))
        self.screen.blit(self.score_tank2, (500, 820))


    def create_map(self):
        for row, tiles in enumerate(wall.wall_map):
            for col, tile in enumerate(tiles):
                if tile == 1:
                    wall.Wall(self.wall_group, col, row)
    
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

