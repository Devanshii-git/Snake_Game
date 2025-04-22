import random


def update_snake_position(snake_x, snake_y, vel_x, vel_y):
    return snake_x + vel_x, snake_y + vel_y


def check_food_collision(snake_x, snake_y, food_x, food_y):
    return abs(snake_x - food_x) <= 16 and abs(snake_y - food_y) <= 16


def generate_food(screen_width, screen_height, margin=20):
    # Ensure food spawns strictly within non-border areas (leaving 20px safe zone)
    food_x = random.randint(margin + 10, screen_width - margin - 30)
    food_y = random.randint(margin + 10, screen_height - margin - 30)

    # Round positions to nearest multiple of 10 for alignment
    food_x = (food_x // 10) * 10
    food_y = (food_y // 10) * 10

    return food_x, food_y



def is_collision_with_wall(x, y, screen_width, screen_height, border=5):
    return (
        x < border or
        x > screen_width - border - 20 or
        y < border or
        y > screen_height - border - 20
    )


def is_collision_with_self(snk_list):
    return snk_list[-1] in snk_list[:-1]
