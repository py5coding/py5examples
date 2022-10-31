"""
Acceleration with Vectors
by Daniel Shiffman.

Demonstration of the basics of motion with vector.
A "Mover" object stores location, velocity, and acceleration as vectors
The motion is controlled by affecting the acceleration (in this case towards the mouse)
"""

# The Mover tracks location, velocity, and acceleration


class Mover(object):

    def __init__(self):
        self.acceleration = None
        # Start in the center
        self.location = Py5Vector(width / 2, height / 2)
        self.velocity = Py5Vector(0, 0)
        self.topspeed = 5

    def update(self):
        # Compute a vector that points from location to mouse
        mouse = Py5Vector(mouse_x, mouse_y)
        self.acceleration = mouse - self.location
        # Set magnitude of acceleration
        self.acceleration.set_mag(0.2)
        # Velocity changes according to acceleration
        self.velocity += self.acceleration
        # Limit the velocity by topspeed
        self.velocity.limit(self.topspeed)
        # Location changes by velocity
        self.location += self.velocity

    def display(self):
        stroke(255)
        stroke_weight(2)
        fill(127)
        ellipse(self.location.x, self.location.y, 48, 48)
