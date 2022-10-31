class Egg(object):

    def __init__(self, xpos, ypos, t, s):
        self.x = xpos  # x-coordinate
        self.y = ypos  # y-coordinate
        self.tilt = t  # Left and right angle offset
        self.angle = 0  # Used to define the tilt
        self.scalar = s / 100.0  # Height of the egg

    def wobble(self):
        self.tilt = cos(self.angle) / 8
        self.angle += 0.1

    def display(self):
        no_stroke()
        fill(255)
        with push_matrix():
            translate(self.x, self.y)
            rotate(self.tilt)
            scale(self.scalar)
            with begin_shape():
                vertex(0, -100)
                bezier_vertex(25, -100, 40, -65, 40, -40)
                bezier_vertex(40, -15, 25, 0, 0, 0)
                bezier_vertex(-25, 0, -40, -15, -40, -40)
                bezier_vertex(-40, -65, -25, -100, 0, -100)
