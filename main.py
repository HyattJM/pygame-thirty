
import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (10, 10, 25)
FPS = 60

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong x Breakout")
clock = pygame.time.Clock()

# Game objects
paddle = Paddle(WIDTH // 2, HEIGHT - 30)
ball = Ball(WIDTH // 2, HEIGHT // 2)
bricks = []

# Create grid of bricks
rows, cols = 5, 10
for row in range(rows):
    for col in range(cols):
        x = 60 + col * 70
        y = 50 + row * 30
        color = (255 - row * 30, 100 + row * 20, 200)
        bricks.append(Brick(x, y, color=color))

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    paddle.move(keys, WIDTH)
    paddle.draw(screen)

    ball.move()
    ball.bounce_off_paddle(paddle.rect)
    ball.draw(screen)

    # Brick collision
    for brick in bricks:
        if brick.alive and ball.get_rect().colliderect(brick.rect):
            brick.hit()
            ball.speed_y *= -1
            break  # Only hit one brick per frame

    # Draw bricks
    for brick in bricks:
        brick.draw(screen)

    pygame.display.flip()

pygame.quit()
