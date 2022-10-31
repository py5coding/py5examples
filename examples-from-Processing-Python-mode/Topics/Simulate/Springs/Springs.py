"""
Springs.

Move the mouse over one of the circles and click to re-position.
When you release the mouse, it will snap back into position.
Each circle has a slightly different behavior.
"""

springs = []
num = 3


def setup():
    size(640, 360)
    no_stroke()
    springs.append(Spring(240, 260, 40, 0.98, 8.0, 0.1, springs))
    springs.append(Spring(320, 210, 120, 0.95, 9.0, 0.1, springs))
    springs.append(Spring(180, 170, 200, 0.90, 9.9, 0.1, springs))


def draw():
    background(51)
    for spring in springs:
        spring.update()
        spring.display()


def mouse_pressed():
    for spring in springs:
        spring.pressed()


def mouse_released():
    for spring in springs:
        spring.released()


class Spring(object):

    # Constructor

    def __init__(self, x, y, s, d, m, k_in, others):
        self.over = False
        self.move = False
        self.velx = 0.0  # X Velocity
        self.vely = 0.0  # Y Velocity
        self.accel = 0  # Acceleration
        self.force = 0  # Force
        # Screen values
        self.xpos = x
        self.tempxpos = x
        self.ypos = y
        self.tempypos = y
        self.rest_posx = x  # Rest position X
        self.rest_posy = y  # Rest position Y
        self.size = s
        self.damp = d  # Damping
        self.mass = m  # Mass
        self.k = k_in  # Spring constant
        self.friends = others

    def update(self):
        if self.move:
            self.rest_posy = mouse_y
            self.rest_posx = mouse_x
        self.force = -self.k * (self.tempypos - self.rest_posy)  # f=-ky
        # Set the acceleration, f=ma == a=f/m
        self.accel = self.force / self.mass
        self.vely = self.damp * (self.vely + self.accel)  # Set the velocity
        self.tempypos = self.tempypos + self.vely  # Updated position
        self.force = -self.k * (self.tempxpos - self.rest_posx)  # f=-ky
        # Set the acceleration, f=ma == a=f/m
        self.accel = self.force / self.mass
        self.velx = self.damp * (self.velx + self.accel)  # Set the velocity
        self.tempxpos = self.tempxpos + self.velx  # Updated position
        self.over = (self.over_event() or self.move) and not self.other_over()

    # Test to see if mouse is over this spring
    def over_event(self):
        dis_x = self.tempxpos - mouse_x
        dis_y = self.tempypos - mouse_y
        return sqrt(sq(dis_x) + sq(dis_y)) < self.size / 2

    # Make sure no other springs are active
    def other_over(self):
        for friend in self.friends:
            if friend != self and friend.over:
                return True
        return False

    def display(self):
        if self.over:
            fill(153)
        else:
            fill(255)
        ellipse(self.tempxpos, self.tempypos, self.size, self.size)

    def pressed(self):
        self.move = self.over

    def released(self):
        self.move = False
        self.rest_posx = self.xpos
        self.rest_posy = self.ypos
