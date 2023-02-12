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
    # bird list
    bird_list = []
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
                        new_bird = Bird(pos=pos, dir=dir, **params)
                        new_bird.note = 60+i-1
                        bird_list.append(new_bird)
                        # music
                        note_on = [0x90, new_bird.note, 112]
                        midiout.send_message(note_on)

                if event.unicode == '0':
                    pos = note_positions[note_index[10]]
                    dir = note_positions[(note_index[10]+7)%12]-note_positions[note_index[10]]
                    new_bird = Bird(pos=pos, dir=dir, **params)
                    bird_list.append(new_bird)
                    new_bird.note = 70
                    # music
                    note_on = [0x90, new_bird.note, 112]
                    midiout.send_message(note_on)
                if event.unicode == '-':
                    pos = note_positions[note_index[11]]
                    dir = note_positions[(note_index[11]+7)%12]-note_positions[note_index[11]]
                    new_bird = Bird(pos=pos, dir=dir, **params)
                    bird_list.append(new_bird)
                    new_bird.note = 71
                    # music
                    note_on = [0x90, new_bird.note, 112]
                    midiout.send_message(note_on)
                if event.unicode == '=':
                    pos = note_positions[note_index[12]]
                    dir = note_positions[(note_index[12]+7)%12]-note_positions[note_index[12]]
                    new_bird = Bird(pos=pos, dir=dir, **params)
                    bird_list.append(new_bird)
                    new_bird.note = 72
                    # music
                    note_on = [0x90, new_bird.note, 112]
                    midiout.send_message(note_on)
                if event.unicode == ' ':
                    bird_list = []
                    for n in range(21,109):
                        note_off = [0x90, n, 0]
                        midiout.send_message(note_off)


        # --- Logic
        for bird in bird_list:
            # Update bird parameters
            bird.update(bird_list)

            # remove older birds
            if bird.time > LIFETIME:
                bird_list.remove(bird)
                # music
                note_off = [0x90, bird.note, 0]
                midiout.send_message(note_off)

            # new birds
            if bird.hitnote != -1:
                pos = note_positions[note_index[bird.hitnote]]
                dir = note_positions[(note_index[bird.hitnote]+7)%12]-pos
                new_bird = Bird(pos=pos, dir=dir, **params)
                bird_list.append(new_bird)
                new_bird.note = 60 + bird.hitnote - 1
                note_colors[bird.hitnote]=(0,255,0)
                # music
                note_on = [0x90, new_bird.note, 112]
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
        for bird in bird_list:
            points = get_triangle_points(bird.pos,bird.direction(),bird.size, loc=[400,400], scale=350)
            pygame.draw.polygon(screen, bird.color, points)

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


