import random


def update_snake_position(snake_x, snake_y, vel_x, vel_y):
    return snake_x + vel_x, snake_y + vel_y


def check_food_collision(snake_x, snake_y, food_x, food_y):
    return abs(snake_x - food_x) <= 16 and abs(snake_y - food_y) <= 16


def generate_food(screen_width, screen_height):
    return random.randint(20, screen_width - 20), random.randint(20, screen_height - 20)


def is_collision_with_wall(x, y, screen_width, screen_height):
    return x < 0 or x > screen_width or y < 0 or y > screen_height


def is_collision_with_self(snk_list):
    return snk_list[-1] in snk_list[:-1]
