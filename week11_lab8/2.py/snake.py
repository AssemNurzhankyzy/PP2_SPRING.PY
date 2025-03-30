import pygame  
import sys  
import copy  
import random  
import time  

pygame.init()  # Initialize pygame

# Game settings
scale = 15  # Size of snake and food
score = 0  # Player score
level = 0  # Game level
SPEED = 10  # Snake movement speed

food_x = 10  # Initial food x position
food_y = 10  # Initial food y position

display = pygame.display.set_mode((500, 500))  # Game window
pygame.display.set_caption("Snake Game")  # Window title
clock = pygame.time.Clock()  # Game clock

# Colors
background_top = (0, 0, 50)  # Top gradient color
background_bottom = (0, 0, 0)  # Bottom gradient color
snake_colour = (255, 137, 0)  # Snake body color
food_colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # Random food color
snake_head = (255, 247, 0)  # Snake head color
font_colour = (255, 255, 255)  # Score text color
defeat_colour = (255, 0, 0)  # "Game Over" text color

# Snake class
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = scale
        self.h = scale
        self.x_dir = 1  # Moving right initially
        self.y_dir = 0  # No vertical movement initially
        self.history = [[self.x, self.y]]  # Movement history
        self.length = 1  # Initial length

    def reset(self):  # Reset snake on death
        self.x = 500 / 2 - scale
        self.y = 500 / 2 - scale
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def show(self):  # Draw snake
        for i in range(self.length):
            if i == 0:
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self):  # Check if snake eats food
        return abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale

    def check_level(self):  # Check if level increases
        return self.length % 5 == 0

    def grow(self):  # Increase snake length
        self.length += 1
        self.history.append(self.history[self.length - 2])

    def death(self):  # Check if snake hits itself
        for i in range(1, self.length):
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True

    def update(self):  # Update snake position
        for i in range(self.length - 1, 0, -1):
            self.history[i] = copy.deepcopy(self.history[i - 1])
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

# Food class
class Food:
    def new_location(self):  # Generate new food position
        global food_x, food_y
        food_x = random.randrange(1, int(500 / scale) - 1) * scale
        food_y = random.randrange(1, int(500 / scale) - 1) * scale

    def show(self):  # Draw food
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))

# Display score
def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))

# Display level
def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))

# Game loop

def gameLoop():
    global score, level, SPEED
    
    snake = Snake(500 / 2, 500 / 2)
    food = Food()
    food.new_location()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if snake.y_dir == 0:
                    if event.key == pygame.K_UP:
                        snake.x_dir = 0
                        snake.y_dir = -1
                    if event.key == pygame.K_DOWN:
                        snake.x_dir = 0
                        snake.y_dir = 1
                if snake.x_dir == 0:
                    if event.key == pygame.K_LEFT:
                        snake.x_dir = -1
                        snake.y_dir = 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_dir = 1
                        snake.y_dir = 0

        # Draw background gradient
        for y in range(500):
            color = (
                background_top[0] + (background_bottom[0] - background_top[0]) * y / 500,
                background_top[1] + (background_bottom[1] - background_top[1]) * y / 500,
                background_top[2] + (background_bottom[2] - background_top[2]) * y / 500
            )
            pygame.draw.line(display, color, (0, y), (500, y))

        snake.show()
        snake.update()
        food.show()
        show_score()
        show_level()

        if snake.check_eaten():
            food.new_location()
            score += random.randint(1, 5)
            snake.grow()
        
        if snake.check_level():
            food.new_location()
            level += 1
            SPEED += 1
            snake.grow()

        if snake.death():
            score = 0
            level = 0
            font = pygame.font.SysFont(None, 100)
            text = font.render("Game Over!", True, defeat_colour)
            display.blit(text, (50, 200))
            pygame.display.update()
            time.sleep(3)
            snake.reset()

        # Screen wrapping
        if snake.history[0][0] > 500:
            snake.history[0][0] = 0
        if snake.history[0][0] < 0:
            snake.history[0][0] = 500
        if snake.history[0][1] > 500:
            snake.history[0][1] = 0
        if snake.history[0][1] < 0:
            snake.history[0][1] = 500

        pygame.display.update()
        clock.tick(SPEED)

gameLoop()
