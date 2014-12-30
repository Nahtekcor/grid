
 
import pygame
import block_new
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

WIDTH = 20
HEIGHT = 20
MARGIN = 5
pygame.init()
all_sprites_list = []
def drawgrid(C, W, H, M):
    x_start = 100
    for i in range(10):
        new = block_new.Block(C, W, H)
        new.set_coord(screen, x_start, 0)
        all_sprites_list.append(new)
# Set the width and height of the screen [width, height]
size = (255, 255)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
#this function draws the grid
drawgrid(WHITE, WIDTH, HEIGHT, MARGIN)
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    for items in len(all_sprites_list):
        all_sprites_list[items].draw
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
