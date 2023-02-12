# Imports
# ---------------------------
import numpy as np
import pygame


# Parameters
# ---------------------------
# used to make animation
mp4 = False
# velocity of birds
vel = 14
# field of vision
field = 75
# bird size
bird_SIZE = 8
# size of screen
screen_size = [800, 800]
# initial list of birds
bird_list=[]
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
        if mp4 == True:
            filename = 'animation/'+'capture_'+str(i)+'.jpeg'
            pygame.image.save(screen, filename)

        # --- Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Background
        screen.fill((0,0,0))

        # --- Logic
        for bird in bird_list:
            # remove older birds
            if bird.time() > 100:
                bird_list.remove(bird)

            # change bird positions and velocities based on rules
            bird.update()

        # --- Drawing
        for bird in bird_list:
            pygame.draw.polygon(screen, bird.color(), bird.points())

        # --- Wrap-up (Limit to 60 frames per second)
        clock.tick(20)

        # --- Update screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()


