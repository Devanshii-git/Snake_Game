import random

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

class SnakeGame:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = RIGHT
        self.generate_food()
        self.score = 0
        self.game_over = False

    def generate_food(self):
        while True:
            self.food = (
                random.randint(0, self.width - 1),
                random.randint(0, self.height - 1)
            )
            if self.food not in self.snake:
                break

    def change_direction(self, new_direction):
        opposite_directions = {
            UP: DOWN,
            DOWN: UP,
            LEFT: RIGHT,
            RIGHT: LEFT
        }
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

   
