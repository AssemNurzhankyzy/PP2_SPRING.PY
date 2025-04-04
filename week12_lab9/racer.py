# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialize Pygame
pygame.init()

# Game Constants
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0

# Coin thresholds to increase speed
COIN_THRESHOLDS = [10, 20, 30, 40, 50]
speed_increased_at = set()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background
background = pygame.image.load("AnimatedStreet.png")

# Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1, 2, 3])  # 1 = light, 3 = heavy
        self.original_image = pygame.image.load("coin.png")
        self.update_image()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(100, SCREEN_HEIGHT - 100))

    def update_image(self):
        size = 20 + self.weight * 10
        self.image = pygame.transform.scale(self.original_image, (size, size))

    def reset(self):
        self.weight = random.choice([1, 2, 3])
        self.update_image()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(100, SCREEN_HEIGHT - 100))

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, 5)

# Initialize sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Background movement
background_y = 0

# Clock
FramePerSec = pygame.time.Clock()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Check player-enemy collision
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(RED)
        screen.blit(game_over, (100, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Background scrolling
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Draw Score and Coin Counter
    screen.blit(font_small.render(f"Score: {SCORE}", True, BLACK), (10, 10))
    screen.blit(font_small.render(f"Coins: {COINS}", True, BLACK), (SCREEN_WIDTH - 110, 10))

    # Move and draw all sprites
    P1.move()
    E1.move()

    screen.blit(P1.image, P1.rect)
    screen.blit(E1.image, E1.rect)

    for coin in coins:
        screen.blit(coin.image, coin.rect)

    # Check player-coin collision
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            COINS += coin.weight
            coin.reset()

            # Increase speed after reaching coin thresholds
            for t in COIN_THRESHOLDS:
                if COINS >= t and t not in speed_increased_at:
                    SPEED += 1
                    speed_increased_at.add(t)

    pygame.display.update()
    FramePerSec.tick(FPS)
