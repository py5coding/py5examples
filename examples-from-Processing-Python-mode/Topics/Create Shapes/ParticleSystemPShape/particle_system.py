# The Particle System
from py5 import * # this might need change in the future {{1}}
from particle import Particle


class ParticleSystem(object):

    def __init__(self, n):
        # It's just a list of particle objects.
        self.particles = []
        # The PShape to group all the particle PShapes.
        self.particle_shape = create_shape(GROUP)
        # Make all the Particles.
        sprite = load_image("sprite.png")
        for i in range(n):
            p = Particle(sprite)
            self.particles.append(p)
            # Each particle's PShape gets added to the System PShape.
            self.particle_shape.add_child(p.get_shape())

    def update(self):
        for p in self.particles:
            p.update()

    def set_emitter(self, x, y):
        for p in self.particles:
            # Each particle gets reborn at the emitter location.
            if p.is_dead():
                p.rebirth(x, y)

    def display(self):
        shape(self.particle_shape)
