# The Boid class
class Boid(object):

    def __init__(self, x, y):
        self.acceleration = Py5Vector(0, 0)
        self.angle = random(TWO_PI)
        self.velocity = Py5Vector(cos(self.angle), sin(self.angle))
        self.location = Py5Vector(x, y)
        self.r = 2.0
        self.maxspeed = 2
        self.maxforce = 0.03

    def run(self, boids):
        self.flock(boids)
        self.update()
        self.borders()
        self.render()

    def apply_force(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration += force

    # We accumulate acceleration each time based on three rules.
    def flock(self, boids):
        sep = self.separate(boids)  # Separation
        ali = self.align(boids)  # Alignment
        coh = self.cohesion(boids)  # Cohesion
        # Arbitrarily weight these forces.
        sep *= 1.5
        ali *= 1.0
        coh *= 1.0
        # Add the force vectors to acceleration.
        self.apply_force(sep)
        self.apply_force(ali)
        self.apply_force(coh)

    # Method to update location.
    def update(self):
        # Update velocity.
        self.velocity += self.acceleration
        # Limit speed.
        self.velocity.limit(self.maxspeed)
        self.location += self.velocity
        # Reset accelertion to 0 each cycle.
        self.acceleration *= 0

    # A method that calculates and applies a steering force towards a target.
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        # A vector pointing from the location to the target.
        desired = target - self.location
        # Scale to maximum speed.
        desired.normalize()
        desired *= self.maxspeed
        # Above two lines of code below could be condensed with PVector setMag() method.
        # Not using this method until Processing.js catches up.
        # desired.setMag(maxspeed)
        # Steering = Desired minus Velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force.
        return steer

    def render(self):
        # Draw a triangle rotated in the direction of velocity.
        theta = self.velocity.heading2_d() + radians(90)
        # heading2D() above is now heading() but leaving old syntax until
        # Processing.js catches up.
        fill(200, 100)
        stroke(255)
        with push_matrix():
            translate(self.location.x, self.location.y)
            rotate(theta)
            with begin_shape(TRIANGLES):
                vertex(0, -self.r * 2)
                vertex(-self.r, self.r * 2)
                vertex(self.r, self.r * 2)

    # Wraparound
    def borders(self):
        if self.location.x < -self.r:
            self.location.x = width + self.r
        if self.location.y < -self.r:
            self.location.y = height + self.r
        if self.location.x > width + self.r:
            self.location.x = -self.r
        if self.location.y > height + self.r:
            self.location.y = -self.r

    # Separation
    # Method checks for nearby boids and steers away.
    def separate(self, boids):
        desiredseparation = 25.0
        steer = Py5Vector(0, 0, 0)
        count = 0
        # For every boid in the system, check if it's too close.
        for other in boids:
            d = PVector.dist(self.location, other.location)
            # If the distance is greater than 0 and less than an arbitrary
            # amount (0 when you are yourself).
            if 0 < d < desiredseparation:
                # Calculate vector pointing away from neighbor.
                diff = self.location - other.location
                diff.normalize()
                diff /= d  # Weight by distance.
                steer += diff
                count += 1  # Keep track of how many
        # Average -- divide by how many
        if count == 0:
            return Py5Vector(0, 0)
        if count > 0:
            steer /= float(count)
        # As long as the vector is greater than 0
        if steer.mag > 0:
            # First two lines of code below could be condensed with PVector setMag() method.
            # Implement Reynolds: Steering = Desired - Velocity
            steer.normalize()
            steer *= self.maxspeed
            steer -= self.velocity
            steer.limit(self.maxforce)
        return steer

    # Alignment
    # For every nearby boid in the system, calculate the average velocity.
    def align(self, boids):
        neighbordist = 50
        sum = Py5Vector(0, 0)
        count = 0
        for other in boids:
            d = PVector.dist(self.location, other.location)
            if 0 < d < neighbordist:
                sum += other.velocity
                count += 1
        if count == 0:
            return Py5Vector(0, 0)
        sum /= float(count)
        # First two lines of code below could be condensed with PVector setMag() method.
        # Implement Reynolds: Steering = Desired - Velocity
        sum.normalize()
        sum *= self.maxspeed
        steer = sum - self.velocity
        steer.limit(self.maxforce)
        return steer

    # Cohesion
    # For the average location (i.e. center) of all nearby boids, calculate
    # steering vector towards that location.
    def cohesion(self, boids):
        neighbordist = 50
        # Start with empty vector to accumulate all locations.
        sum = Py5Vector(0, 0)
        count = 0
        for other in boids:
            d = PVector.dist(self.location, other.location)
            if 0 < d < neighbordist:
                sum += other.location  # Add location.
                count += 1
        if count > 0:
            sum /= count
            return self.seek(sum)  # Steer towards the location.
        else:
            return Py5Vector(0, 0)
