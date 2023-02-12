# Imports
# ---------------------------
import numpy as np
import pygame
import rtmidi
from birds import *
from params import *


# Pygame
# ---------------------------
def main():
    """
    This is our main program.
    """
    pygame.init()
    # Mido
    midiout = rtmidi.MidiOut()
    midiout.open_virtual_port('foo')
    #port = mido.open_output(name='foo', virtual=True)
    # Set the height and width of the screen
    screen = pygame.display.set_mode(screen_size)
    # Caption
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

            # Keydown - for notes
            if event.type == pygame.KEYDOWN:
                for i in range(1,10):
                    if event.unicode == str(i):
                        pos = note_positions[note_index[i]]
                        dir = note_positions[(note_index[i]+7)%12]-note_positions[note_index[i]]
                        new_boid = Bird(pos=pos, dir=dir, **params)
                        new_boid.note = 60+i-1
                        boid_list.append(new_boid)
                        # music
                        note_on = [0x90, new_boid.note, 112]
                        midiout.send_message(note_on)

                if event.unicode == '0':
                    pos = note_positions[note_index[10]]
                    dir = note_positions[(note_index[10]+7)%12]-note_positions[note_index[10]]
                    new_boid = Bird(pos=pos, dir=dir, **params)
                    boid_list.append(new_boid)
                    new_boid.note = 70
                    # music
                    note_on = [0x90, new_boid.note, 112]
                    midiout.send_message(note_on)
                if event.unicode == '-':
                    pos = note_positions[note_index[11]]
                    dir = note_positions[(note_index[11]+7)%12]-note_positions[note_index[11]]
                    new_boid = Bird(pos=pos, dir=dir, **params)
                    boid_list.append(new_boid)
                    new_boid.note = 71
                    # music
                    note_on = [0x90, new_boid.note, 112]
                    midiout.send_message(note_on)
                if event.unicode == '=':
                    pos = note_positions[note_index[12]]
                    dir = note_positions[(note_index[12]+7)%12]-note_positions[note_index[12]]
                    new_boid = Bird(pos=pos, dir=dir, **params)
                    boid_list.append(new_boid)
                    new_boid.note = 72
                    # music
                    note_on = [0x90, new_boid.note, 112]
                    midiout.send_message(note_on)
                if event.unicode == ' ':
                    boid_list = []
                    for n in range(21,109):
                        note_off = [0x90, n, 0]
                        midiout.send_message(note_off)


        # --- Logic
        for boid in boid_list:
            # Update boid parameters
            boid.update(boid_list)

            # remove older boids
            if boid.time > LIFETIME:
                boid_list.remove(boid)
                # music
                note_off = [0x90, boid.note, 0]
                midiout.send_message(note_off)

            # new boids
            if boid.hitnote != -1:
                pos = note_positions[note_index[boid.hitnote]]
                dir = note_positions[(note_index[boid.hitnote]+7)%12]-pos
                new_boid = Bird(pos=pos, dir=dir, **params)
                boid_list.append(new_boid)
                new_boid.note = 60 + boid.hitnote - 1
                note_colors[boid.hitnote]=(0,255,0)
                # music
                note_on = [0x90, new_boid.note, 112]
                midiout.send_message(note_on)

        # --- Drawing the Background
        screen.fill((0,0,0))

        # --- Drawing the Star Pattern
        for i in range(1,13):
            pos = vector_transform(note_positions[note_index[i]], loc=400, scale=350)
            pygame.draw.circle(screen, color=note_colors[i], center=pos, radius=15)
            font = pygame.font.SysFont(None, 24)
            img = font.render(str(i), True,BLACK)
            screen.blit(img, pos-np.array([8,8]))
            
        # --- Drawing the Birds
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


