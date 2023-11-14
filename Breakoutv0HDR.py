import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game variables
paddle_width, paddle_height = 100, 20
ball_radius = 10
brick_width, brick_height = 60, 30

# Paddle
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 40, paddle_width, paddle_height)

# Ball
ball = pygame.Rect(WIDTH // 2 - ball_radius // 2, HEIGHT // 2 - ball_radius // 2, ball_radius, ball_radius)
ball_speed_x, ball_speed_y = 3 * random.choice((-1, 1)), 3 * random.choice((-1, 1))  # Slower ball speed

# Bricks
bricks = [pygame.Rect(c * brick_width, r * brick_height, brick_width, brick_height) for r in range(3) for c in range(WIDTH // brick_width)]

# Frame rate
clock = pygame.time.Clock()
fps = 30  # Lower frame rate for a more Atari-like experience

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-5, 0)  # Slower paddle movement
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(5, 0)  # Slower paddle movement

    # Ball movement
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Ball collision with bricks
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y *= -1
            break

    # Game over conditions
    if ball.bottom >= HEIGHT:
        running = False

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Update display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(fps)

pygame.quit()
## [C] GPL-3.0-or-later
