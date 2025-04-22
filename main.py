import pygame
import random
from ui import *
from backend import *
from controls import *

pygame.init()
pygame.mixer.init()

def game_over(score):
    RUN = False
    while not RUN:
        window = show_game_over_screen(score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                RUN = True
                show_tutorial_screen()
                gameloop()

def generate_food(screen_width, screen_height, margin=20):
    food_x = random.randint(margin + 10, screen_width - margin - 30)
    food_y = random.randint(margin + 10, screen_height - margin - 30)
    return food_x, food_y

def gameloop():
    pygame.mixer.music.load("assets/sounds/bgm.mp3")
    pygame.mixer.music.play(-1)

    start_sound = pygame.mixer.Sound("assets/sounds/start.wav")
    eat_sound = pygame.mixer.Sound("assets/sounds/eat.wav")
    gameover_sound = pygame.mixer.Sound("assets/sounds/gameover.wav")
    turn_sound = pygame.mixer.Sound("assets/sounds/turn.wav")

    start_sound.play()
    screen_width, screen_height = 750, 650
    snake_x, snake_y = screen_width / 2, screen_height / 2
    snake_w, snake_h = 20, 20
    vel_x, vel_y = 0, 0
    food_x, food_y = generate_food(screen_width, screen_height)
    snk_list, snk_length = [], 1
    score = 0
    fps = 240
    clock = pygame.time.Clock()

    window = create_window(screen_width, screen_height, "Jai Shri Krishna")
    exit_game = False

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            vel_x, vel_y = handle_keys(event, vel_x, vel_y)
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                    turn_sound.play()

        if check_food_collision(snake_x, snake_y, food_x, food_y):
            food_x, food_y = generate_food(screen_width, screen_height)
            snk_length += 20
            score += 1
            eat_sound.play()

        snake_x, snake_y = update_snake_position(snake_x, snake_y, vel_x, vel_y)
        snk_list.append([snake_x, snake_y])
        if len(snk_list) > snk_length:
            del snk_list[0]

        if is_collision_with_wall(snake_x, snake_y, screen_width, screen_height) or is_collision_with_self(snk_list):
            pygame.mixer.music.stop()
            gameover_sound.play()
            pygame.time.delay(1000)
            game_over(score)

        window.fill((255, 255, 255))
        pygame.draw.rect(window, (0, 0, 0), [0, 0, screen_width, screen_height], 10)
        draw_snake(window, snk_list, snake_w)
        draw_food(window, food_x, food_y, snake_w, snake_h)
        draw_score(window, score)
        pygame.display.update()
        clock.tick(fps)


if __name__ == "__main__":
    show_tutorial_screen()
    gameloop()
