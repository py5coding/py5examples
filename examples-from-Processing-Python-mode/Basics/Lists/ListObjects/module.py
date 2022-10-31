class MovingBall(object):

    # Constructor
    def __init__(self, x_offset, y_offset, x, y, speed, unit):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.x = x
        self.y = y
        self.speed = speed
        self.unit = unit
        self.x_direction = 1
        self.y_direction = 1

    # Custom method for updating the variables
    def update(self):
        self.x += (self.speed * self.x_direction)
        if self.x >= self.unit or self.x <= 0:
            self.x_direction *= -1
            self.x += self.x_direction
            self.y += self.y_direction
        if self.y >= self.unit or self.y <= 0:
            self.y_direction *= -1
            self.y += self.y_direction

    # Custom method for drawing the object
    def draw(self):
        fill(255)
        ellipse(self.x_offset + self.x, self.y_offset + self.y, 6, 6)
