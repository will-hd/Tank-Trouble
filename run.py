import pygame
import numpy as np
from tank import Tank

# Initialise pygame 
pygame.init()

DISPLAY_WIDTH =  800
DISPLAY_HEIGHT = 600

# Create screen
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
backdrop = pygame.Surface([DISPLAY_WIDTH, DISPLAY_HEIGHT])
backdrop_box = screen.get_rect()

# Instantiate a tank and sprite group
tank = Tank()
tank_group = pygame.sprite.Group()
tank_group.add(tank)

# Game loop
GAME_RUNNING = True
while GAME_RUNNING:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUNNING = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        tank.control(0.1, 0)
    if keys[pygame.K_LEFT]:
        tank.control(-0.1, 0)
    if keys[pygame.K_UP]:
        tank.control(0, -0.1)
    if keys[pygame.K_DOWN]:
        tank.control(0, +0.1)

    screen.blit(backdrop, backdrop_box)
    tank.update()
    tank_group.draw(screen)

    pygame.display.update()