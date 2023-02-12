# Imports
import numpy as np
from birds import *

# Parameters
# ---------------------------
# used to make animation
MP4 = False
# speed of boids
SPEED = 0.01
# Boid size
SIZE = 0.04
# COLOR
COLOR = (0,206,209)
# WHITE
WHITE = (255,255,255)
# BLACK
BLACK = (0,0,0)
# LIFETIME
LIFETIME=360
# FIELD
FIELD = 0.3
# size of screen
screen_size = [800, 800]
# Star positions
note_positions = star_positions()
# dictionnary of indices for notes
note_index = {i:(i+6)%12 for i in range(1,13)}
# color palette
color_palette = {
    '1':(69, 66, 235),
    '2':(250, 2, 2),
    '3':(69, 66, 235),
    '4':(250, 2, 2),
    '5':(69, 66, 235),
    '6':(250, 2, 2),
    '7':(69, 66, 235),
    '8':(250, 2, 2),
    '9':(69, 66, 235),
    '10':(250, 2, 2),
    '11':(69, 66, 235),
    '12':(250, 2, 2),
}
# ----------------------------


params = {'speed':SPEED,
            'size':SIZE,
            'color':COLOR,
            'field':FIELD}