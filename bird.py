# Imports
import numpy as np



# Positions of the 12 notes
def star_positions(center, radius):
    notes = [1,2,3,4,5,6,7,8,9,10,11,12]
    


# Class to generate Birds
class Bird:
    def __init__(self, x0, y0, dir, speed, color):
        self.x0 = x0
        self.y0 = y0
        self.pos = np.array([x0, y0])
        self.velocity = speed * dir
        self.color = color
        
