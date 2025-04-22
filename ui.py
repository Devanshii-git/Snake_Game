import pygame

# Colors
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


def create_window(width, height, caption):
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return window


def draw_snake(window, snk_list, size):
    GREEN = (0, 255, 0)
    for i, (x, y) in enumerate(snk_list):
        pygame.draw.rect(window, GREEN, [x, y, size, size])

    # Head Details
    if snk_list:
        head_x, head_y = snk_list[-1]
        eye_radius = 3
        tongue_length = 10

        # Eyes
        eye_color = (255, 255, 255)
        left_eye_pos = (head_x + 5, head_y + 5)
        right_eye_pos = (head_x + size - 5, head_y + 5)
        pygame.draw.circle(window, eye_color, left_eye_pos, eye_radius)
        pygame.draw.circle(window, eye_color, right_eye_pos, eye_radius)

        # Tongue
        tongue_color = (255, 0, 0)
        tongue_start = (head_x + size // 2, head_y + size)
        tongue_end = (head_x + size // 2,)




def draw_food(window, x, y, width, height):
    radius = width // 2
    center_x = x + radius
    center_y = y + radius
    pygame.draw.circle(window, YELLOW, (center_x, center_y), radius)


def show_game_over_screen(score):
    width, height = 750, 650
    window = create_window(width, height, "Game Over")

    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over! Press Enter to play again", True, (255, 0, 0))
    score_text = font.render(f"Your Score: {score}", True, (0, 0, 0))

    text_rect = text.get_rect(center=(width // 2, height // 2 - 30))
    score_rect = score_text.get_rect(center=(width // 2, height // 2 + 30))

    window.fill((255, 255, 255))
    window.blit(text, text_rect)
    window.blit(score_text, score_rect)
    pygame.display.update()

    return window


def show_tutorial_screen():
    window = create_window(800, 700, "Welcome to Snake Game!")
    font_big = pygame.font.Font("freesansbold.ttf", 40)
    font_small = pygame.font.Font("freesansbold.ttf", 25)

    title = font_big.render("Welcome to the Snake Game!", True, YELLOW)
    line1 = font_small.render("Use Arrow Keys to move the Snake.", True, BLUE)
    line2 = font_small.render("Eat the yellow food to grow longer.", True, BLUE)
    line3 = font_small.render("Avoid hitting the walls or yourself.", True, BLUE)
    line4 = font_small.render("Reversing into the snake causes Game Over.", True, BLUE)
    line5 = font_small.render("Press Enter to Start or click Exit to quit.", True, GREEN)

    # Exit Button
    button_font = pygame.font.Font("freesansbold.ttf", 25)
    exit_text = button_font.render("Exit", True, BLACK)
    exit_rect = pygame.Rect(350, 500, 100, 50)  # (x, y, width, height)

    window.fill(BLACK)
    window.blit(title, title.get_rect(center=(400, 120)))
    window.blit(line1, line1.get_rect(center=(400, 220)))
    window.blit(line2, line2.get_rect(center=(400, 270)))
    window.blit(line3, line3.get_rect(center=(400, 320)))
    window.blit(line4, line4.get_rect(center=(400, 370)))
    window.blit(line5, line5.get_rect(center=(400, 450)))

    # Draw Exit Button
    pygame.draw.rect(window, YELLOW, exit_rect)
    window.blit(exit_text, exit_text.get_rect(center=exit_rect.center))

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()

def draw_score(window, score):
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    window.blit(score_text, (10, 10))