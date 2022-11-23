import pygame
import numpy as np

# Initialise pygame 
pygame.init()

DISPLAY_WIDTH =  800
DISPLAY_HEIGHT = 600

# Create screen
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))


# Player
player_image = pygame.image.load('icon.png')
PLAYER_POSTION = np.array([200, 200])
dPOSITION = np.array([0, 0])

def player(position):
    screen.blit(player_image, position)

# Game loop
GAME_RUNNING = True
while GAME_RUNNING:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUNNING = False

        # # If keystroke pressed, check if left or right
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         dPLAYER_X = -0.1 
        #     if event.key == pygame.K_RIGHT:
        #         dPLAYER_X = 0.1
        # # if event.type == pygame.KEYUP:
        # #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        # #         dPLAYER_X = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        dPOSITION[0] = dPOSITION[0] + 0.1
    if keys[pygame.K_LEFT]:
        dPOSITION[0] += -0.1
    if keys[pygame.K_UP]:
        dPOSITION[1] += 0.1
    if keys[pygame.K_DOWN]:
        dPOSITION[1] += -0.1
    print(dPOSITION[0])
    PLAYER_POSTION += dPOSITION

    player(PLAYER_POSTION)
    pygame.display.update()

    dPOSITION = np.array([0,0])

