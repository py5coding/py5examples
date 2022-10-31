class Ball(object):
    # Class variables. These are shared amongst all instances of Ball.
    Spring = 0.05
    Gravity = 0.03
    Friction = -0.9

    def __init__(self, x, y, radius, index, others):
        self.x = x
        self.y = y
        self.radius = radius
        self.index = index
        self.others = others
        self.vx = 0
        self.vy = 0

    def collide(self):
        for other in self.others[self.index:]:
            dx = other.x - self.x
            dy = other.y - self.y
            min_dist = other.radius + self.radius
            if dist(other.x, other.y, self.x, self.y) < min_dist:
                angle = atan2(dy, dx)
                target_x = self.x + cos(angle) * min_dist
                target_y = self.y + sin(angle) * min_dist
                ax = (target_x - other.x) * Ball.Spring
                ay = (target_y - other.y) * Ball.Spring
                self.vx -= ax
                self.vy -= ay
                other.vx += ax
                other.vy += ay

    def move(self):
        self.vy += Ball.Gravity
        self.x += self.vx
        self.y += self.vy

        if self.x + self.radius > width:
            self.x = width - self.radius
            self.vx *= Ball.Friction
        elif self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= Ball.Friction
        if self.y + self.radius > height:
            self.y = height - self.radius
            self.vy *= Ball.Friction
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= Ball.Friction

    def display(self):
        ellipse(self.x, self.y, self.radius, self.radius)
