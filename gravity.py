# Imports
# ---------------------------
import numpy as np
import pygame
from birds import *


# Parameters
# ---------------------------
# used to make animation
MP4 = False
# speed of boids
SPEED = 14
# Boid size
SIZE = 8
# COLOR
COLOR = (0,206,209)
# size of screen
screen_size = [800, 800]
# Star positions
note_positions = star_positions()
# initial list of boids
boid_list=[Bird(pos=[1,0], dir=[1,0], speed=SPEED, size=SIZE, color=COLOR)]
# ----------------------------


# Pygame Loop
# ---------------------------
def main():
    """
    This is our main program.
    """
    pygame.init()

    # Set the height and width of the screen
    screen = pygame.display.set_mode(screen_size)

    pygame.display.set_caption("Visualization")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()


    # -------- Main Program Loop -----------
    i = 0
    while not done:
        i+=1

        # --- Animation
        if MP4 == True:
            filename = 'animation/'+'capture_'+str(i)+'.jpeg'
            pygame.image.save(screen, filename)

        # --- Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Background
        screen.fill((0,0,0))

        # --- Logic
        for boid in boid_list:
            # remove older boids
            if boid.time > 100:
                boid_list.remove(boid)

            # change boid positions and velocities based on rules
            boid.update()

        # --- Drawing
        for boid in boid_list:
            pygame.draw.polygon(screen, boid.color, boid.points())

        # --- Wrap-up (Limit to 60 frames per second)
        clock.tick(20)

        # --- Update screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()


