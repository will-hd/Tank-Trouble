import pygame
import numpy as np

# Initialise pygame 
pygame.init()

DISPLAY_WIDTH =  800
DISPLAY_HEIGHT = 600

# Create screen
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))


class Tank:
    def __init__(self) -> None:
        self.player_image = pygame.image.load('icon.png')
        self.POSITION = np.array([200, 200], dtype=np.float32)
        self.dPOSITION = np.array([0, 0], dtype=np.float32)

    def move(self):
        self.POSITION += self.dPOSITION
        self.dPOSITION = np.array([0, 0], dtype='float32') # Reset back to zero for next frame

        # Convert to integer for pygame drawing
        integer_position = self.POSITION.astype(int)
        screen.blit(self.player_image, integer_position)

# Instantiate a tank
tank = Tank()

# Game loop
GAME_RUNNING = True
while GAME_RUNNING:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUNNING = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        tank.dPOSITION[0] += 0.1
    if keys[pygame.K_LEFT]:
        tank.dPOSITION[0] += -0.1
    if keys[pygame.K_UP]:
        tank.dPOSITION[1] += -0.1
    if keys[pygame.K_DOWN]:
        tank.dPOSITION[1] += 0.1

    tank.move()
    pygame.display.update()