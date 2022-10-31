# A simple Particle class
class Particle(object):

    def __init__(self, l):
        self.acceleration = Py5Vector(0, 0.05)
        self.velocity = Py5Vector(random(-1, 1), random(-2, 0))
        self.location = l.get()
        self.lifespan = 255.0

    def run(self):
        self.update()
        self.display()

    # Method to update location
    def update(self):
        self.velocity += self.acceleration
        self.location += self.velocity
        self.lifespan -= 2.0

    # Method to display
    def display(self):
        stroke(255, self.lifespan)
        fill(255, self.lifespan)
        ellipse(self.location.x, self.location.y, 8, 8)

    # Is the particle still useful?
    def is_dead(self):
        return self.lifespan < 0.0
