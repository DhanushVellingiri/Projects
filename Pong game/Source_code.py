import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BRICK_WIDTH, BRICK_HEIGHT = 75, 20
BACKGROUND_COLOR = (0, 0, 0)
BALL_COLOR = (255, 255, 255)
PADDLE_COLOR = (255, 0, 0)
BRICK_COLOR = (0, 255, 0)
FPS = 60

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Breakout")

# Create game objects
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_SIZE // 2, WINDOW_HEIGHT - 60, BALL_SIZE, BALL_SIZE)
ball_dx, ball_dy = 5, -5
paddle = pygame.Rect(WINDOW_WIDTH // 2 - PADDLE_WIDTH // 2, WINDOW_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)
bricks = [pygame.Rect(i * (BRICK_WIDTH + 10) + 30, j * (BRICK_HEIGHT + 10) + 30, BRICK_WIDTH, BRICK_HEIGHT) 
          for i in range(10) for j in range(5)]

# Clock for controlling the frame rate
clock = pygame.time.Clock()

def draw_objects():
    window.fill(BACKGROUND_COLOR)
    pygame.draw.ellipse(window, BALL_COLOR, ball)
    pygame.draw.rect(window, PADDLE_COLOR, paddle)
    for brick in bricks:
        pygame.draw.rect(window, BRICK_COLOR, brick)
    pygame.display.flip()

def main():
    global ball_dx, ball_dy

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= 10
        if keys[pygame.K_RIGHT] and paddle.right < WINDOW_WIDTH:
            paddle.x += 10

        ball.x += ball_dx
        ball.y += ball_dy

        if ball.left <= 0 or ball.right >= WINDOW_WIDTH:
            ball_dx *= -1
        if ball.top <= 0:
            ball_dy *= -1
        if ball.bottom >= WINDOW_HEIGHT:
            pygame.quit()
            sys.exit()

        if ball.colliderect(paddle):
            ball_dy *= -1

        for brick in bricks[:]:
            if ball.colliderect(brick):
                ball_dy *= -1
                bricks.remove(brick)

        draw_objects()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
