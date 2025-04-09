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

    def update(self):
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        new_head = {
            UP: (head_x, head_y - 1),
            DOWN: (head_x, head_y + 1),
            LEFT: (head_x - 1, head_y),
            RIGHT: (head_x + 1, head_y),
        }[self.direction]

        if not (0 <= new_head[0] < self.width) or not (0 <= new_head[1] < self.height):
            self.game_over = True
            return

        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.generate_food()
        else:
            self.snake.pop()  # remove tail

    def get_game_state(self):
        return {
            'snake': self.snake,
            'food': self.food,
            'score': self.score,
            'game_over': self.game_over
        }

   
