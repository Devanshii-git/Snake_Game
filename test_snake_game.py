import unittest
import pygame
from backend import *
from controls import handle_keys
from main import generate_food

class TestBackend(unittest.TestCase):
    def test_check_food_collision(self):
        snake_x, snake_y = 100, 100
        food_x, food_y = 100, 100
        self.assertTrue(check_food_collision(snake_x, snake_y, food_x, food_y))

        food_x, food_y = 200, 200
        self.assertFalse(check_food_collision(snake_x, snake_y, food_x, food_y))

    def test_update_snake_position(self):
        x, y = 100, 100
        vx, vy = 10, 0
        new_x, new_y = update_snake_position(x, y, vx, vy)
        self.assertEqual((new_x, new_y), (110, 100))

    def test_is_collision_with_wall(self):
        screen_width, screen_height = 750, 650
        self.assertTrue(is_collision_with_wall(0, 300, screen_width, screen_height))
        self.assertTrue(is_collision_with_wall(300, 0, screen_width, screen_height))
        self.assertFalse(is_collision_with_wall(100, 100, screen_width, screen_height))

    def test_is_collision_with_self(self):
        snake = [[100, 100], [110, 100], [120, 100], [100, 100]]
        self.assertTrue(is_collision_with_self(snake))

        snake = [[100, 100], [110, 100], [120, 100], [130, 100]]
        self.assertFalse(is_collision_with_self(snake))

class TestControls(unittest.TestCase):
    def test_handle_keys(self):
        pygame.init()
        pygame.display.set_mode((1, 1))  # Required to use key events
        test_keys = [
            (pygame.K_RIGHT, (1, 0)),
            (pygame.K_LEFT, (-1, 0)),
            (pygame.K_UP, (0, -1)),
            (pygame.K_DOWN, (0, 1)),
        ]
        for key, expected in test_keys:
            event = pygame.event.Event(pygame.KEYDOWN, {'key': key})
            with self.subTest(key=key):
                vx, vy = handle_keys(event, 0, 0)
                self.assertEqual((vx, vy), expected)

class TestMain(unittest.TestCase):
    def test_generate_food_bounds(self):
        screen_width, screen_height = 750, 650
        margin = 20
        for _ in range(100):
            food_x, food_y = generate_food(screen_width, screen_height, margin)
            with self.subTest(food_x=food_x, food_y=food_y):
                in_bounds = (
                    margin + 10 <= food_x <= screen_width - margin - 30 and
                    margin + 10 <= food_y <= screen_height - margin - 30
                )
                self.assertTrue(in_bounds, f"Food at ({food_x}, {food_y}) should not spawn on the border.")

if __name__ == '__main__':
    unittest.main()
