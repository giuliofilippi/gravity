# Imports
# ---------------------------
import numpy as np
import pygame
from birds import *


# Parameters
# ---------------------------
# used to make animation
MP4 = False
# Gravity strenght
mu = 0
# speed of boids
SPEED = 0.01
# Boid size
SIZE = 0.04
# COLOR
COLOR = (0,206,209)
# LIFETIME
LIFETIME=360
# size of screen
screen_size = [800, 800]
# Star positions
note_positions = star_positions()
# dictionnary of indices for notes
note_index = {i:(i+6)%12 for i in range(1,13)}
# initial list of boids
boid_list=[
Bird(pos=[0,0], dir=[-1,0], speed=SPEED, size=SIZE, color=COLOR, mu=mu),
Bird(pos=[0,0], dir=[1,0], speed=SPEED, size=SIZE, color=COLOR, mu=mu),
Bird(pos=[0,0], dir=[0,1], speed=SPEED, size=SIZE, color=COLOR, mu=mu),
Bird(pos=[0,0], dir=[0,-1], speed=SPEED, size=SIZE, color=COLOR, mu=mu)
]
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

            # keydown - for notes
            if event.type == pygame.KEYDOWN:
                print(event)
                for i in range(1,10):
                    if event.unicode == str(i):
                        pos = note_positions[note_index[i]]
                        dir = note_positions[(note_index[i]+7)%12]-note_positions[note_index[i]]
                        new_boid = Bird(pos=pos, dir=dir, speed=SPEED, size=SIZE, color=COLOR, mu=mu)
                        boid_list.append(new_boid)
                if event.unicode == '0':
                    pos = note_positions[note_index[10]]
                    dir = note_positions[(note_index[10]+7)%12]-note_positions[note_index[10]]
                    new_boid = Bird(pos=pos, dir=dir, speed=SPEED, size=SIZE, color=COLOR, mu=mu)
                    boid_list.append(new_boid)
                if event.unicode == '-':
                    pos = note_positions[note_index[11]]
                    dir = note_positions[(note_index[11]+7)%12]-note_positions[note_index[11]]
                    new_boid = Bird(pos=pos, dir=dir, speed=SPEED, size=SIZE, color=COLOR, mu=mu)
                    boid_list.append(new_boid)
                if event.unicode == '=':
                    pos = note_positions[note_index[12]]
                    dir = note_positions[(note_index[12]+7)%12]-note_positions[note_index[12]]
                    new_boid = Bird(pos=pos, dir=dir, speed=SPEED, size=SIZE, color=COLOR, mu=mu)
                    boid_list.append(new_boid)

        # --- Background
        screen.fill((0,0,0))

        # --- Logic
        for boid in boid_list:
            # remove older boids
            if boid.time > LIFETIME:
                boid_list.remove(boid)

            # change boid positions and velocities based on rules
            boid.update()

        # --- Drawing
        for boid in boid_list:
            points = get_triangle_points(boid.pos,boid.direction(),boid.size, loc=[400,400], scale=350)
            pygame.draw.polygon(screen, boid.color, points)

        # --- Wrap-up (Limit to 60 frames per second)
        clock.tick(30)

        # --- Update screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()


