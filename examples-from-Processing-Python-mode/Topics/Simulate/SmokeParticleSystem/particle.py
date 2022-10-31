
# A simple Particle class, renders the particle as an image.


class Particle(object):

    def __init__(self, l, img):
        self.acc = Py5Vector(0, 0)
        self.vx = random_gaussian() * 0.3
        self.vy = random_gaussian() * 0.3 - 1.0
        self.vel = Py5Vector(self.vx, self.vy)
        self.loc = l.get()
        self.lifespan = 100.0
        self.img = img

    def run(self):
        self.update()
        self.render()

    # Method to apply a force vector to the Particle object
    # Note we are ignoring "mass" here.
    def apply_force(self, f):
        self.acc += f

    # Method to update location
    def update(self):
        self.vel += self.acc
        self.loc += self.vel
        self.lifespan -= 2.5
        self.acc *= 0  # clear Acceleration.

    # Method to display
    def render(self):
        image_mode(CENTER)
        tint(255, self.lifespan)
        image(self.img, self.loc.x, self.loc.y)
        # Drawing a circle instead.
        # fill(255,lifespan)
        # noStroke()
        # ellipse(self.loc.x,self.loc.y,self.img.width,self.img.height)

    # Is the particle still useful?
    def is_dead(self):
        return self.lifespan <= 0.0
