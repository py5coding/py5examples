class Orb(object):
    # A damping of 80% slows it down when it hits the ground.
    Damping = 0.8
    Gravity = Py5Vector(0, 0.05)

    def __init__(self, x, y, radius):
        # Orb has position and velocity.
        self.position = Py5Vector(x, y)
        self.velocity = Py5Vector(0.5, 0)
        self.radius = radius

    def move(self):
        # Move orb.
        self.velocity += Orb.Gravity
        self.position += self.velocity

    def display(self):
        # Draw orb.
        no_stroke()
        fill(200)
        ellipse(
            self.position.x,
            self.position.y,
            self.radius * 2,
            self.radius * 2)

    # Check boundaries of window.
    def check_wall_collision(self):
        if self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -Orb.Damping

        elif self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= -Orb.Damping

    def check_ground_collision(self, ground):

        # Get difference between orb and ground.
        delta_x = self.position.x - ground.x
        delta_y = self.position.y - ground.y

        # Precalculate trig values.
        cosine = cos(ground.rot)
        sine = sin(ground.rot)

        # Rotate ground and velocity to allow orthogonal collision.
        #  calculations
        ground_x_temp = cosine * delta_x + sine * delta_y
        ground_y_temp = cosine * delta_y - sine * delta_x
        velocity_x_temp = cosine * self.velocity.x + sine * self.velocity.y
        velocity_y_temp = cosine * self.velocity.y - sine * self.velocity.x

        # Ground collision - check for surface collision and also that orb is
        #  within left / right bounds of ground segment.
        if (ground_y_temp > -self.radius and
            self.position.x > ground.x1 and
                self.position.x < ground.x2):
            # keep orb from going into ground.
            ground_y_temp = -self.radius
            # bounce and slow down orb.
            velocity_y_temp *= -1.0
            velocity_y_temp *= Orb.Damping

        # Reset ground, velocity and orb.
        delta_x = cosine * ground_x_temp - sine * ground_y_temp
        delta_y = cosine * ground_y_temp + sine * ground_x_temp
        self.velocity.x = cosine * velocity_x_temp - sine * velocity_y_temp
        self.velocity.y = cosine * velocity_y_temp + sine * velocity_x_temp
        self.position.x = ground.x + delta_x
        self.position.y = ground.y + delta_y
