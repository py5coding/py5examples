# An individual Particle
from py5 import *  # this might need change in the future {{1}}

class Particle(object):

    def __init__(self, sprite):
        # A single force
        self.gravity = Py5Vector(0, 0.1)
        self.part_size = random(10, 60)
        # The particle is a textured quad.
        self.part = create_shape()
        self.part.begin_shape(QUAD)
        self.part.no_stroke()
        self.part.texture(sprite)
        self.part.normal(0, 0, 1)
        self.part.vertex(-self.part_size / 2, -self.part_size / 2, 0, 0)
        self.part.vertex(self.part_size / 2,
                         -self.part_size / 2, sprite.width, 0)
        self.part.vertex(self.part_size / 2,
                         self.part_size / 2, sprite.width, sprite.height)
        self.part.vertex(-self.part_size / 2,
                         self.part_size / 2, 0, sprite.height)
        self.part.end_shape()
        # Initialize center vector.
        self.center = Py5Vector(0, 0)
        # Set the particle starting location.
        width = get_current_sketch().width
        height = get_current_sketch().height
        self.rebirth(width / 2, height / 2)

    def get_shape(self):
        return self.part

    def rebirth(self, x, y):
        a = random(TWO_PI)
        speed = random(0.5, 4)
        # A velocity with random angle and magnitude.
        self.velocity = Py5Vector.from_heading(a)
        self.velocity *= speed
        # Set lifespan.
        self.lifespan = 255
        # Set location using translate.
        self.part.reset_matrix()
        self.part.translate(x, y)
        # Update center vector.
        self.center.xy = (x, y)

    # Is it off the screen, or its lifespan is over?
    def is_dead(self):
        width = get_current_sketch().width
        height = get_current_sketch().height
        return (self.center.x > width or self.center.x < 0
                or self.center.y > height or self.center.y < 0 or
                self.lifespan < 0)

    def update(self):
        # Decrease life.
        self.lifespan = self.lifespan - 1
        # Apply gravity.
        self.velocity += self.gravity
        self.part.set_tint(color(255, self.lifespan))
        # Move the particle according to its velocity,
        self.part.translate(self.velocity.x, self.velocity.y)
        # and also update the center
        self.center += self.velocity
