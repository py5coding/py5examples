class Hair(object):
    def __init__(self, radius):
        self.radius = radius
        self.phi = random(TAU)
        self.slow = random(1.15, 1.2)
        self.theta = asin(random(-self.radius, self.radius) / self.radius)
        self.z = self.radius * sin(self.theta)

    def render(self):
        o_ff = (noise(millis() * 0.0005, sin(self.phi)) - 0.5) * 0.3
        o_f_fb = (noise(millis() * 0.0007, sin(self.z) * 0.01) - 0.5) * 0.3

        self.theta_ff = self.theta + o_ff
        phi_ff = self.phi + o_f_fb
        x = self.radius * cos(self.theta) * cos(self.phi)
        y = self.radius * cos(self.theta) * sin(self.phi)
        self.z = self.radius * sin(self.theta)

        xo = self.radius * cos(self.theta_ff) * cos(phi_ff)
        yo = self.radius * cos(self.theta_ff) * sin(phi_ff)
        zo = self.radius * sin(self.theta_ff)

        xb = xo * self.slow
        yb = yo * self.slow
        zb = zo * self.slow

        with begin_shape(LINES):
            stroke(0)
            vertex(x, y, self.z)
            stroke(200, 150)
            vertex(xb, yb, zb)
