import pygame
import math

# Initialize pygame
pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Enhanced Paint")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Drawing settings
drawing_color = BLACK
bg_color = WHITE
tool = "pen"  # Default tool
line_width = 5
start_pos = None

# Drawing canvas
canvas = pygame.Surface((screen_width, screen_height))
canvas.fill(bg_color)

# Font for tool labels
font = pygame.font.SysFont('Arial', 16)

# Color palette setup
color_palette = [BLACK, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE]
palette_rects = []
palette_x, palette_y = 10, 10
palette_size = 30
palette_padding = 5

# Generate palette buttons
for i, color in enumerate(color_palette):
    rect = pygame.Rect(
        palette_x + i * (palette_size + palette_padding),
        palette_y,
        palette_size,
        palette_size
    )
    palette_rects.append(rect)

# Tool buttons
tool_buttons = {
    "pen": pygame.Rect(10, 50, 100, 30),
    "rectangle": pygame.Rect(10, 85, 100, 30),
    "circle": pygame.Rect(10, 120, 100, 30),
    "square": pygame.Rect(10, 155, 100, 30),
    "right_triangle": pygame.Rect(10, 190, 100, 30),
    "equilateral_triangle": pygame.Rect(10, 225, 100, 30),
    "rhombus": pygame.Rect(10, 260, 100, 30),
    "eraser": pygame.Rect(10, 295, 100, 30)
}

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse button press
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                # Color palette selection
                for i, rect in enumerate(palette_rects):
                    if rect.collidepoint(event.pos):
                        drawing_color = color_palette[i]
                        if tool == "eraser":
                            tool = "pen"  # Switch back to pen when color is selected

                # Tool selection
                for tool_name, rect in tool_buttons.items():
                    if rect.collidepoint(event.pos):
                        tool = tool_name
                        if tool == "eraser":
                            drawing_color = bg_color

                # Start position for drawing shapes
                start_pos = event.pos
                if tool == "pen" or tool == "eraser":
                    pygame.draw.circle(canvas, drawing_color, event.pos, line_width)

        # Handle mouse movement for pen/eraser
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  # Left button held
                if tool == "pen" or tool == "eraser":
                    pygame.draw.line(canvas, drawing_color, start_pos, event.pos, line_width * 2)
                    start_pos = event.pos

        # Handle mouse button release
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos:
                end_pos = event.pos

                x1, y1 = start_pos
                x2, y2 = end_pos

                # Rectangle tool
                if tool == "rectangle":
                    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(canvas, drawing_color, rect, line_width)

                # Circle tool
                elif tool == "circle":
                    radius = int(math.hypot(x2 - x1, y2 - y1))
                    pygame.draw.circle(canvas, drawing_color, start_pos, radius, line_width)

                # Square tool (constrained rectangle)
                elif tool == "square":
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    rect = pygame.Rect(x1, y1, side, side)
                    pygame.draw.rect(canvas, drawing_color, rect, line_width)

                # Right Triangle
                elif tool == "right_triangle":
                    points = [start_pos, (x2, y1), end_pos]
                    pygame.draw.polygon(canvas, drawing_color, points, line_width)

                # Equilateral Triangle
                elif tool == "equilateral_triangle":
                    side = math.dist(start_pos, end_pos)
                    height = (math.sqrt(3) / 2) * side
                    points = [
                        (x1, y1),
                        (x1 + side, y1),
                        (x1 + side / 2, y1 - height)
                    ]
                    pygame.draw.polygon(canvas, drawing_color, points, line_width)

                # Rhombus
                elif tool == "rhombus":
                    dx = (x2 - x1) // 2
                    dy = (y2 - y1) // 2
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    points = [
                        (center_x, y1),       # Top
                        (x2, center_y),       # Right
                        (center_x, y2),       # Bottom
                        (x1, center_y)        # Left
                    ]
                    pygame.draw.polygon(canvas, drawing_color, points, line_width)

                start_pos = None

    # Clear screen
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    # Draw palette
    for color, rect in zip(color_palette, palette_rects):
        pygame.draw.rect(screen, color, rect)
        if color == drawing_color:
            pygame.draw.rect(screen, BLACK, rect, 2)  # Outline current color

    # Draw tool buttons
    for tool_name, rect in tool_buttons.items():
        btn_color = (200, 200, 200)
        if tool == tool_name:
            btn_color = (150, 150, 150)
        pygame.draw.rect(screen, btn_color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)
        label = font.render(tool_name.replace("_", " ").capitalize(), True, BLACK)
        screen.blit(label, (rect.x + 5, rect.y + 5))

    # Show tool and color status
    status_text = f"Tool: {tool.replace('_', ' ').capitalize()} | Color: {drawing_color}"
    text_surface = font.render(status_text, True, BLACK)
    screen.blit(text_surface, (screen_width - text_surface.get_width() - 10, 10))

    pygame.display.flip()

pygame.quit()
