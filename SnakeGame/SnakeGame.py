# Import python game helper
import pygame

# Set window dimensions in pixels
window_x = 1200
window_y = 600

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

    # Display the window at 60fps
    pygame.display.update()
    fps.tick(60)
