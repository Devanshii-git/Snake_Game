import pygame
from ui import *
from backend import *
from controls import *

pygame.init()


def game_over():
    RUN = False
    while not RUN:
        window = show_game_over_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                RUN = True
                show_tutorial_screen()  # 👈 Show tutorial after Game Over
                gameloop()


def gameloop():
    # Initial Setup
    screen_width, screen_height = 750, 650
    snake_x, snake_y = screen_width / 2, screen_height / 2
    snake_w, snake_h = 20, 20
    vel_x, vel_y = 0, 0
    food_x, food_y = generate_food(screen_width, screen_height)
    snk_list, snk_length = [], 1
    fps = 240
    clock = pygame.time.Clock()

    window = create_window(screen_width, screen_height, "Jai Shri Krishna")
    exit_game = False

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            vel_x, vel_y = handle_keys(event, vel_x, vel_y)

        if check_food_collision(snake_x, snake_y, food_x, food_y):
            food_x, food_y = generate_food(screen_width, screen_height)
            snk_length += 20

        snake_x, snake_y = update_snake_position(snake_x, snake_y, vel_x, vel_y)
        snk_list.append([snake_x, snake_y])
        if len(snk_list) > snk_length:
            del snk_list[0]

        if is_collision_with_wall(snake_x, snake_y, screen_width, screen_height) or is_collision_with_self(snk_list):
            game_over()

        window.fill((0, 0, 0))
        draw_snake(window, snk_list, snake_w,)
        draw_food(window, food_x, food_y, snake_w, snake_h)
        pygame.display.update()
        clock.tick(fps)


show_tutorial_screen()
gameloop()
