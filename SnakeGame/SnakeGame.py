# Import python game helper
import pygame

# Set grid dimensions in pixels
grid_width = 1200
grid_height = 600

# Number of squares the grid is wide
grid_width_in_squares = 30

# Square size
square_size = grid_width // grid_width_in_squares

# Set window dimensions in pixels
window_width = grid_width
window_height = grid_height + 60

# Define important colours in RBG values
white = pygame.Color(255, 255, 255)
gray = pygame.Color(200, 200, 200)
black = pygame.Color(0, 0, 0)

# Start the game helper
pygame.init()

# Create the game window
pygame.display.set_caption("Snake")
game_window = pygame.display.set_mode((window_width, window_height))

fps = pygame.time.Clock()

# Display game controls
def show_controls(color, font, size):
    controls_font = pygame.font.SysFont(font, size)
    controls_surface = controls_font.render("WASD or ARROWS to Move", True, color)
    game_window.blit(controls_surface, (495, window_height - 40))

# Game loop
while True:
    # Able the window if you want/need
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()    

    # White background
    game_window.fill(white)

    # Game Grid
    for x in range(0, grid_width, square_size):
        for y in range(0, grid_height, square_size):
            pygame.draw.rect(game_window, gray, pygame.Rect(x, y, square_size, square_size), 1)

    # Box for bottom text
    pygame.draw.rect(game_window, gray, pygame.Rect(0, grid_height, grid_width, grid_height))
    pygame.draw.line(game_window, black, (0, grid_height), (grid_width, grid_height), 2)

    # Display control text
    show_controls(black, "Arial", 20)

    # Display the window at 60fps
    pygame.display.update()
    fps.tick(60)
