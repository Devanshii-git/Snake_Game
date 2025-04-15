import pygame


def handle_keys(event, vel_x, vel_y):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            return 1, 0
        elif event.key == pygame.K_LEFT:
            return -1, 0
        elif event.key == pygame.K_UP:
            return 0, -1
        elif event.key == pygame.K_DOWN:
            return 0, 1
    return vel_x, vel_y
