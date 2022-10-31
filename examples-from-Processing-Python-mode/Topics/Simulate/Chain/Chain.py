"""
Chain.

One mass is attached to the mouse position and the other
is attached the position of the other mass. The gravity
in the environment pulls down on both.
"""
gravity = 9.0
mass = 2.0


def setup():
    global s1, s2
    size(640, 360)
    fill(255, 126)
    s1 = Spring2D(0.0, width / 2, mass, gravity)
    s2 = Spring2D(0.0, width / 2, mass, gravity)


def draw():
    background(0)
    s1.update(mouse_x, mouse_y)
    s1.display(mouse_x, mouse_y)
    s2.update(s1.x, s1.y)
    s2.display(s1.x, s1.y)


class Spring2D(object):

    def __init__(self, xpos, ypos, m, g):
        # The x- and y-axis velocities
        self.vx = 0.0
        self.vy = 0.0
        # The x- and y-coordinates
        self.x = xpos
        self.y = ypos
        self.radius = 30
        self.stiffness = 0.2
        self.damping = 0.7
        self.mass = m
        self.gravity = g

    def update(self, target_x, target_y):
        force_x = (target_x - self.x) * self.stiffness
        ax = force_x / self.mass
        self.vx = self.damping * (self.vx + ax)
        self.x += self.vx
        force_y = (target_y - self.y) * self.stiffness
        force_y += self.gravity
        ay = force_y / self.mass
        self.vy = self.damping * (self.vy + ay)
        self.y += self.vy

    def display(self, nx, ny):
        no_stroke()
        ellipse(self.x, self.y, self.radius * 2, self.radius * 2)
        stroke(255)
        line(self.x, self.y, nx, ny)
