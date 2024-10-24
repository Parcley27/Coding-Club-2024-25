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

# Initial Game Setup
highscore = 0
score = 0

# Display current score
def score_display(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    game_window.blit(score_surface, (20, window_height - 40))

# Display game controls
def controls_display(color, font, size):
    controls_font = pygame.font.SysFont(font, size)
    controls_surface = controls_font.render("WASD or ARROWS to Move", True, color)
    game_window.blit(controls_surface, (495, window_height - 40))

# Display highscore
def highscore_display(color, font, size):
    highscore_font = pygame.font.SysFont(font, size)
    highscore_surface = highscore_font.render("Highscore: " + str(highscore), True, color)
    game_window.blit(highscore_surface, (window_width - 110, window_height - 40))

# Game loop
while True:
    # Close the window if you want/need
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

    # Display bottom text
    score_display(black, "Arial", 20)
    controls_display(black, "Arial", 20)
    highscore_display(black, "Arial", 20)

    # Display the window at 60fps
    pygame.display.update()
    fps.tick(60)
