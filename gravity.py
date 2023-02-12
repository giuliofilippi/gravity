# Imports
# ---------------------------
import numpy as np
import pygame
from birds import *
from params import *

# Pygame
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
    # Boid list
    boid_list = []
    # color of note circles
    note_colors = note_palette.copy()

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
                for i in range(1,10):
                    if event.unicode == str(i):
                        pos = note_positions[note_index[i]]
                        dir = note_positions[(note_index[i]+7)%12]-note_positions[note_index[i]]
                        new_boid = Bird(pos=pos, dir=dir, **params)
                        boid_list.append(new_boid)
                if event.unicode == '0':
                    pos = note_positions[note_index[10]]
                    dir = note_positions[(note_index[10]+7)%12]-note_positions[note_index[10]]
                    new_boid = Bird(pos=pos, dir=dir, **params)
                    boid_list.append(new_boid)
                if event.unicode == '-':
                    pos = note_positions[note_index[11]]
                    dir = note_positions[(note_index[11]+7)%12]-note_positions[note_index[11]]
                    new_boid = Bird(pos=pos, dir=dir, **params)
                    boid_list.append(new_boid)
                if event.unicode == '=':
                    pos = note_positions[note_index[12]]
                    dir = note_positions[(note_index[12]+7)%12]-note_positions[note_index[12]]
                    new_boid = Bird(pos=pos, dir=dir, **params)
                    boid_list.append(new_boid)

        # --- Logic
        for boid in boid_list:
            # Update boid parameters
            boid.update(boid_list)

            # remove older boids
            if boid.time > LIFETIME:
                boid_list.remove(boid)

            # new boids
            if boid.outnote != -1:
                pos = note_positions[note_index[boid.outnote]]
                dir = note_positions[(note_index[boid.outnote]+7)%12]-pos
                new_boid = Bird(pos=pos, dir=dir, **params)
                boid_list.append(new_boid)
                note_colors[boid.hitnote]=(0,255,0)

        # --- Background
        screen.fill((0,0,0))

        # --- Drawing the Star Pattern
        for i in range(1,13):
            pos = vector_transform(note_positions[note_index[i]], loc=400, scale=350)
            pygame.draw.circle(screen, color=note_colors[i], center=pos, radius=15)
            font = pygame.font.SysFont(None, 24)
            img = font.render(str(i), True,BLACK)
            screen.blit(img, pos-np.array([8,8]))
            
        
        # --- Drawing the birds
        for boid in boid_list:
            points = get_triangle_points(boid.pos,boid.direction(),boid.size, loc=[400,400], scale=350)
            pygame.draw.polygon(screen, boid.color, points)

        # --- Reset some params
        note_colors = note_palette.copy()

        # --- Wrap-up (Limit to 60 frames per second)
        clock.tick(30)

        # --- Update screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()


