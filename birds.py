# Imports
import numpy as np

# Positions of the 12 notes
def star_positions():
    notes = [1,2,3,4,5,6,7,8,9,10,11,12]
    angles = [2*np.pi*(i-5)/12+np.pi/12 for i in notes]
    positions = [np.array([np.cos(ang), np.sin(ang)]) for ang in angles]
    return positions

# Normalize a vector
def normalize(v):
    v = np.array(v)
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

# Position transform
def vector_transform(x, loc, scale):
    return np.array(x)*scale + loc

# distance between boids
def distance(bird1, bird2):
    dx = (bird1.pos-bird2.pos)[0]
    dy = (bird1.pos-bird2.pos)[1]
    return np.linalg.norm(np.array([dx,dy]))

# Get the points of triangle based on position and velocity vector
def get_triangle_points(pos, direction, size, loc, scale):
    normal = np.array([direction[1],-direction[0]])
    loc = np.array(loc)
    x1 = (pos + direction * size)*scale+loc
    x2 = (pos - normal * size/4)*scale+loc
    x3 = (pos + normal * size/4)*scale+loc
    return [x1,x2,x3]

def compute_hit_and_new(pos):
    angle = np.angle(pos[0]+pos[1]j)



# Class to generate Birds
class Bird:
    # Initialise Object
    def __init__(self, pos, dir, speed, size, color, field):
        self.pos = np.array(pos)
        self.speed = speed
        self.velocity = speed * normalize(np.array(dir))
        self.size = size
        self.color = color
        self.field = field
        self.time = 0
        self.hitnote = -1
        self.outnote = -1

    # Direction from velocity
    def direction(self):
        vec = np.array([self.velocity[0],self.velocity[1]])
        vel = np.linalg.norm(vec)
        return vec/vel

    # Neighbours of a boid
    def neighbours(self, list_of_boids):
        neighbours = []
        for brd in list_of_boids:
            if distance(self,brd)<self.field and brd!=self:
                neighbours.append(brd)
        return neighbours

    # Cohesion: we change a boids velocity based on neighbouring boids center of mass
    def cohesion_update(self, neighbours, gamma=0.0004):
        N = len(neighbours)
        if N==0:
            com = self.pos
        else:
            com = sum([x.pos for x in neighbours])/N
        delta_v = normalize(com - self.pos)*gamma
        self.velocity += delta_v
        return self

    # Separation : nearby boids repel each other
    def separation_update(self, neighbours, gamma=0.0001):
        delta_v = np.array([0,0])
        for bird in neighbours:
            if distance(self,bird)<2*self.size:
                delta_v = delta_v + normalize(self.pos - bird.pos)*gamma
        self.velocity += delta_v
        return self
        
    # Gravity : boids gravitational attraction to origin
    def gravitational_update(self, gamma=0.00013):
        origin = np.array([0,0])
        delta_v = normalize(origin - self.pos)*gamma
        self.velocity += delta_v
        return self

    # Acceleration / Deceleration
    def acceleration_update(self):
        current_speed = np.linalg.norm(self.velocity)
        self.velocity += (self.velocity/current_speed)*(self.speed - current_speed)/10
        return self

    def bound_update(self):
        R = np.linalg.norm(self.pos)
        if R>0.96 and self.time>20:
            self.time = 360
            self.hitnote, self.outnote = compute_hit_and_new(self.pos)
        return self
        
    # Final update changing all parameters
    def update(self, list_of_boids):

        # Find neighbours of boid
        neighbours = self.neighbours(list_of_boids)

        # Gravitational Update
        #self.gravitational_update()

        # Cohesion Update
        self.cohesion_update(neighbours)

        # Separation Update
        self.separation_update(neighbours)

        # Acceleration Updates
        self.acceleration_update()

        # Position Updates
        self.pos = self.pos + self.velocity

        # Out of bounds Update
        self.bound_update()

        # Time update
        self.time += 1

        return self
        