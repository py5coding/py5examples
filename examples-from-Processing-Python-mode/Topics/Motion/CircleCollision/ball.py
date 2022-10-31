from py5 import *

class Ball(object):

    def __init__(self, x, y, radius):
        self.position = Py5Vector(x, y)
        self.velocity = Py5Vector.random(2)
        self.velocity *= 3
        self.radius = radius
        self.m = self.radius * 0.1

    def update(self):
        self.position += self.velocity

    def check_boundary_collision(self):
        s =get_current_sketch()
        width, height = s.width, s.height 
        if self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -1
        elif self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= -1
        elif self.position.y > height - self.radius:
            self.position.y = height - self.radius
            self.velocity.y *= -1
        elif self.position.y < self.radius:
            self.position.y = self.radius
            self.velocity.y *= -1

    def check_collision(self, other):
        # Get distances between the balls components.
        b_vect = other.position - self.position

        # Calculate magnitude of the vector separating the balls.
        b_vect_mag = b_vect.mag
        if b_vect_mag < self.radius + other.radius:
            # Get angle of bVect.
            theta = b_vect.heading

            # Precalculate trig values.
            sine = sin(theta)
            cosine = cos(theta)

            # bTemp will hold rotated ball positions. You just need to worry
            #  about bTemp[1] position.
            b_temp = [Py5Vector(0, 0), Py5Vector(0, 0)]

            # This ball's position is relative to the other so you can use the
            #  vector between them (bVect) as the reference point in the
            #  rotation expressions. bTemp[0].position.x and
            #  bTemp[0].position.y will initialize automatically to 0.0, which
            #  is what you want since b[1] will rotate around b[0].
            b_temp[1].x = cosine * b_vect.x + sine * b_vect.y
            b_temp[1].y = cosine * b_vect.y - sine * b_vect.x

            # Rotate Temporary velocities.
            v_temp = [Py5Vector(0, 0), Py5Vector(0, 0)]
            v_temp[0].x = cosine * self.velocity.x + sine * self.velocity.y
            v_temp[0].y = cosine * self.velocity.y - sine * self.velocity.x
            v_temp[1].x = cosine * other.velocity.x + sine * other.velocity.y
            v_temp[1].y = cosine * other.velocity.y - sine * other.velocity.x

            # Now that velocities are rotated, you can use 1D conservation of
            #  momentum equations to calculate the velocity along the x-
            #  axis.
            v_final = [Py5Vector(0, 0), Py5Vector(0, 0)]

            # Rotated velocity for b[0].
            v_final[0].x = (((self.m - other.m) *
                            v_temp[0].x + 2 * other.m * v_temp[1].x) /
                            (self.m + other.m))
            v_final[0].y = v_temp[0].y

            # Rotated velocity for b[0].
            v_final[1].x = (((other.m - self.m) *
                            v_temp[1].x + 2 * self.m * v_temp[0].x) /
                            (self.m + other.m))
            v_final[1].y = v_temp[1].y

            # Hack to avoid clumping.
            b_temp[0].x += v_final[0].x
            b_temp[1].x += v_final[1].x

            # Rotate ball positions and velocities back Reverse signs in trig
            #  expressions to rotate in the opposite direction.
            # Rotate balls.
            b_final = [Py5Vector(0, 0), Py5Vector(0, 0)]
            b_final[0].x = cosine * b_temp[0].x - sine * b_temp[0].y
            b_final[0].y = cosine * b_temp[0].y + sine * b_temp[0].x
            b_final[1].x = cosine * b_temp[1].x - sine * b_temp[1].y
            b_final[1].y = cosine * b_temp[1].y + sine * b_temp[1].x

            # Update balls to screen position.
            other.position.x = self.position.x + b_final[1].x
            other.position.y = self.position.y + b_final[1].y
            self.position += b_final[0]

            # Update velocities.
            self.velocity.x = cosine * v_final[0].x - sine * v_final[0].y
            self.velocity.y = cosine * v_final[0].y + sine * v_final[0].x
            other.velocity.x = cosine * v_final[1].x - sine * v_final[1].y
            other.velocity.y = cosine * v_final[1].y + sine * v_final[1].x

    def display(self):
        no_stroke()
        fill(204)
        ellipse(
            self.position.x,
            self.position.y,
            self.radius * 2,
            self.radius * 2)
