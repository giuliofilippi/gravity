# Imports
import numpy as np

# Positions of the 12 notes
def star_positions(loc=np.array([0,0]), scale=1):
    notes = [1,2,3,4,5,6,7,8,9,10,11,12]
    angles = [2*np.pi*(i-5)/12+np.pi/12 for i in notes]
    positions = [np.array([np.cos(ang), np.sin(ang)])*scale+loc for ang in angles]
    return positions

# Position transform
def vector_transform(x, loc, scale):
    return np.array(x)*scale + loc

# distance between boids
def distance(bird1, bird2):
    dx = (bird1.pos-bird2.pos)[0]
    dy = (bird1.pos-bird2.pos)[1]
    return np.linalg.norm(np.array([dx,dy]))

# Get the points of triangle based on position and velocity vector
def get_triangle_points(pos,direction,size):
    normal = np.array([direction[1],-direction[0]])
    x1 = pos + direction * size
    x2 = pos - normal * size/4
    x3 = pos + normal * size/4
    return [x1,x2,x3]

# Normalize a vector
def normalize(v):
    v = np.array(v)
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm


# Class to generate Birds
class Bird:
    # Initialise Object
    def __init__(self, pos, dir, speed, size, color):
        self.pos = np.array(pos)
        self.velocity = speed * normalize(np.array(dir))
        self.size = size
        self.color = color
        self.time = 0

    # Direction from velocity
    def direction(self):
        vec = np.array([self.velocity[0],self.velocity[1]])
        vel = np.linalg.norm(vec)
        return vec/vel

    # Points for drawing in pygame
    def points(self):
        return get_triangle_points(self.pos,self.direction(),self.size)

    # Change in velocity from gravity effect
    def gravitational_update(self, dt=0.1):
        R = np.linalg.norm(self.pos)
        force_dir = -normalize(self.pos)
        self.velocity += dt*force_dir/R**2
        return self
        
    # Final update changin all parameters
    def update(self):
        # Gravitational velocity update
        self.gravitational_update(dt=0.1)

        # Update positions
        self.pos = self.pos + self.velocity

        # Time update
        self.time += 1

        return self
        