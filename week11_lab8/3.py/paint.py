import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
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

# Default settings
drawing_color = BLACK
bg_color = WHITE
tool = "pen"  # Can be "pen", "rectangle", "circle", "eraser"
line_width = 5
start_pos = None

# Create a surface for drawing
canvas = pygame.Surface((screen_width, screen_height))
canvas.fill(bg_color)

# Font for UI
font = pygame.font.SysFont('Arial', 16)

# Color palette
color_palette = [
    BLACK, RED, GREEN, BLUE, 
    YELLOW, CYAN, MAGENTA, WHITE
]
palette_rects = []
palette_x = 10
palette_y = 10
palette_size = 30
palette_padding = 5

for i, color in enumerate(color_palette):
    rect = pygame.Rect(
        palette_x + i * (palette_size + palette_padding),
        palette_y,
        palette_size,
        palette_size
    )
    palette_rects.append(rect)

# Tool selection buttons
tool_buttons = {
    "pen": pygame.Rect(10, 50, 80, 30),
    "rectangle": pygame.Rect(10, 85, 80, 30),
    "circle": pygame.Rect(10, 120, 80, 30),
    "eraser": pygame.Rect(10, 155, 80, 30)
}

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Check if color palette was clicked
                for i, rect in enumerate(palette_rects):
                    if rect.collidepoint(event.pos):
                        drawing_color = color_palette[i]
                        if tool == "eraser":
                            tool = "pen"  # Switch back to pen when selecting color
                
                # Check if tool button was clicked
                for tool_name, rect in tool_buttons.items():
                    if rect.collidepoint(event.pos):
                        tool = tool_name
                        if tool == "eraser":
                            drawing_color = bg_color
                
                # Start drawing
                start_pos = event.pos
                if tool == "pen" or tool == "eraser":
                    pygame.draw.circle(canvas, drawing_color, event.pos, line_width)
        
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  # Left mouse button is held down
                if tool == "pen" or tool == "eraser":
                    pygame.draw.line(canvas, drawing_color, start_pos, event.pos, line_width * 2)
                    start_pos = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos:  # Left mouse button released
                end_pos = event.pos
                
                if tool == "rectangle":
                    rect = pygame.Rect(
                        min(start_pos[0], end_pos[0]),
                        min(start_pos[1], end_pos[1]),
                        abs(end_pos[0] - start_pos[0]),
                        abs(end_pos[1] - start_pos[1])
                    )
                    pygame.draw.rect(canvas, drawing_color, rect, line_width)
                
                elif tool == "circle":
                    radius = int(math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2))
                    pygame.draw.circle(canvas, drawing_color, start_pos, radius, line_width)
                
                start_pos = None
    
    # Draw everything
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    
    # Draw color palette
    for i, (color, rect) in enumerate(zip(color_palette, palette_rects)):
        pygame.draw.rect(screen, color, rect)
        if color == drawing_color:
            pygame.draw.rect(screen, BLACK, rect, 2)  # Highlight selected color
    
    # Draw tool buttons
    for tool_name, rect in tool_buttons.items():
        color = (200, 200, 200)
        if tool == tool_name:
            color = (150, 150, 150)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)
        text = font.render(tool_name.capitalize(), True, BLACK)
        screen.blit(text, (rect.x + 5, rect.y + 8))
    
    # Display current tool and color
    status_text = f"Tool: {tool.capitalize()} | Color: {drawing_color}"
    text_surface = font.render(status_text, True, BLACK)
    screen.blit(text_surface, (screen_width - text_surface.get_width() - 10, 10))
    
    pygame.display.flip()

pygame.quit()                                              