import pygame

DISPLAY_HEIGHT = 900
DISPLAY_WIDTH = 800
BLOCKSIZE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BULLET_COLOR = (82, 72, 72)


TANK_COLORS = [
    [(0, 96, 0), (0, 128, 0), (32, 32, 96)],
    [(176, 5, 5), (199, 52, 52), (32, 32, 96)]]

MOVEMENT_KEYS = {
    0: {'CLOCKWISE': pygame.K_RIGHT, 'ANTI-CLOCKWISE': pygame.K_LEFT, 
        'FORWARD': pygame.K_UP, 'BACKWARD': pygame.K_DOWN, 'SHOOT': pygame.K_l},
    1: {'CLOCKWISE': pygame.K_d, 'ANTI-CLOCKWISE': pygame.K_a, 
        'FORWARD': pygame.K_w, 'BACKWARD': pygame.K_s, 'SHOOT': pygame.K_f}
        }

TANK_INIT_POSITIONS = [
    (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2 +100), (600, 100)
]
