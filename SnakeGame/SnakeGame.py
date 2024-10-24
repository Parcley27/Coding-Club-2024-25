# Import python game helper
import pygame

# Set window dimensions in pixels
window_x = 1200
window_y = 600

# Number of squares the grid is wide
grid_width = 30

# Square size
square_size = window_x // 30

# Define important colours in RBG values
white = pygame.Color(255, 255, 255)
gray = pygame.Color(200, 200, 200)

# Start the game helper
pygame.init()

# Create the game window
pygame.display.set_caption("Snake")
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

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
    for x in range(0, window_x, square_size):
        for y in range(0, window_y, square_size):
            pygame.draw.rect(game_window, gray, pygame.Rect(x, y, square_size, square_size), 1)

    # Display the window at 60fps
    pygame.display.update()
    fps.tick(60)
