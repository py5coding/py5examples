class Particle(object):

    def __init__(self, sprite):
        self.gravity = Py5Vector(0, 0.1)
        self.lifespan = 255
        self.velocity = Py5Vector()
        part_size = random(10, 60)
        self.part = create_shape()
        self.part.begin_shape(QUAD)
        self.part.no_stroke()
        self.part.texture(sprite)
        self.part.normal(0, 0, 1)
        self.part.vertex(-part_size / 2, -part_size / 2, 0, 0)
        self.part.vertex(+part_size / 2, -part_size / 2, sprite.width, 0)
        self.part.vertex(+part_size / 2, +part_size / 2,
                         sprite.width, sprite.height)
        self.part.vertex(-part_size / 2, +part_size / 2, 0, sprite.height)
        self.part.end_shape()
        self.rebirth(width / 2, height / 2)
        self.lifespan = random(255)

    def get_shape(self):
        return self.part

    def rebirth(self, x, y):
        a = random(TWO_PI)
        speed = random(0.5, 4)
        self.velocity = Py5Vector(cos(a), sin(a))
        self.velocity *= speed
        self.lifespan = 255
        self.part.reset_matrix()
        self.part.translate(x, y)

    def is_dead(self):
        return self.lifespan < 0

    def update(self):
        self.lifespan -= 1
        self.velocity += self.gravity
        self.part.set_tint(color(255, self.lifespan))
        self.part.translate(self.velocity.x, self.velocity.y)
