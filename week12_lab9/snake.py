import pygame
import sys
import random
import time

pygame.init()

# Constants
SCREEN_SIZE = 500
SCALE = 15
SPEED = 10
FOOD_LIFETIME = 5  # Seconds food lives

# Display setup
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Colors
SNAKE_COLOR = (255, 137, 0)
SNAKE_HEAD_COLOR = (255, 247, 0)
FOOD_COLOR = (255, 0, 0)
FONT_COLOR = (255, 255, 255)
DEFEAT_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)

# Game variables
score = 0
level = 0

# Snake class
class Snake:
    def __init__(self):
        self.body = [[SCREEN_SIZE // 2, SCREEN_SIZE // 2]]
        self.direction = [1, 0]  # Moving right initially
        self.grow_pending = 0

    def move(self):
        head = self.body[0][:]
        head[0] += self.direction[0] * SCALE
        head[1] += self.direction[1] * SCALE

        # Wrap around screen
        head[0] %= SCREEN_SIZE
        head[1] %= SCREEN_SIZE

        self.body.insert(0, head)
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self, amount):
        self.grow_pending += amount

    def draw(self):
        for i, part in enumerate(self.body):
            color = SNAKE_HEAD_COLOR if i == 0 else SNAKE_COLOR
            pygame.draw.rect(screen, color, (*part, SCALE, SCALE))

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def set_direction(self, dx, dy):
        # Prevent reversing into self
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = [dx, dy]

# Food class
class Food:
    def __init__(self):
        self.new_food()

    def new_food(self):
        self.x = random.randint(0, (SCREEN_SIZE - SCALE) // SCALE) * SCALE
        self.y = random.randint(0, (SCREEN_SIZE - SCALE) // SCALE) * SCALE
        self.weight = random.randint(1, 5)
        self.spawn_time = time.time()
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, SCALE, SCALE))
        # Show weight on the food
        font = pygame.font.SysFont(None, 18)
        text = font.render(str(self.weight), True, FONT_COLOR)
        screen.blit(text, (self.x + 2, self.y))

    def is_eaten(self, snake_head):
        return abs(snake_head[0] - self.x) < SCALE and abs(snake_head[1] - self.y) < SCALE

    def expired(self):
        return time.time() - self.spawn_time > FOOD_LIFETIME

# Utility functions
def draw_score():
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Score: {score}", True, FONT_COLOR)
    screen.blit(text, (10, 10))

def draw_level():
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Level: {level}", True, FONT_COLOR)
    screen.blit(text, (110, 10))

def game_over():
    font = pygame.font.SysFont(None, 60)
    text = font.render("Game Over", True, DEFEAT_COLOR)
    screen.blit(text, (SCREEN_SIZE // 2 - 150, SCREEN_SIZE // 2 - 30))
    pygame.display.update()
    pygame.time.wait(3000)

# Main game loop
def main():
    global score, level

    snake = Snake()
    food = Food()
    speed = SPEED

    running = True
    while running:
        screen.fill(BG_COLOR)

        # Input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.set_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.set_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.set_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.set_direction(1, 0)
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        # Snake movement
        snake.move()

        # Check food collision
        if food.is_eaten(snake.body[0]):
            score += food.weight
            snake.grow(food.weight)
            food.new_food()

        # Replace food if expired
        if food.expired():
            food.new_food()

        # Level up logic
        if score // 10 > level:
            level += 1
            speed += 1

        # Draw everything
        snake.draw()
        food.draw()
        draw_score()
        draw_level()

        # Check self collision
        if snake.check_collision():
            game_over()
            score = 0
            level = 0
            main()  # Restart game

        pygame.display.update()
        clock.tick(speed)

# Run game
main()
