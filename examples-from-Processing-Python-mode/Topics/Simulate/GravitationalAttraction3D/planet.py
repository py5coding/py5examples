# Gravitational Attraction (3D)
# Daniel Shiffman <http://www.shiffman.net>
# A class for(object): an orbiting Planet


class Planet(object):

    # Basic physics model (location, velocity, acceleration, mass)
    def __init__(self, m, x, y, z):
        self.mass = m
        self.location = Py5Vector(x, y, z)
        self.velocity = Py5Vector(1, 0)  # Arbitrary starting velocity
        self.acceleration = Py5Vector(0, 0)

    # Newton's 2nd Law (F = M*A) applied
    def apply_force(self, force):
        f = force / self.mass
        self.acceleration += f

    # Our motion algorithm (aka Euler Integration)
    def update(self):
        # Velocity changes according to acceleration.
        self.velocity += self.acceleration
        # Location changes according to velocity.
        self.location += self.velocity
        self.acceleration *= 0

    # Draw the Planet.
    def display(self):
        no_stroke()
        fill(255)
        with push_matrix():
            translate(self.location.x, self.location.y, self.location.z)
            sphere(self.mass * 8)
