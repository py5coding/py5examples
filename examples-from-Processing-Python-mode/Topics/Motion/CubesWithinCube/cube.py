# Custom Cube Class
class Cube(object):
    QuadBG = []
    # Colors are hardcoded
    QuadBG.append(color(255, 0, 0))
    QuadBG.append(color(255, 128, 0))
    QuadBG.append(color(255, 255, 0))
    QuadBG.append(color(0, 255, 0))
    QuadBG.append(color(0, 0, 255))
    QuadBG.append(color(127, 0, 255))

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        # Position, velocity vectors
        # Start in center
        self.position = Py5Vector()
        # Random velocity vector
        self.velocity = Py5Vector.random(3)
        # Also using PVector to hold rotation values for 3 axes
        # Random rotation
        self.rotation = Py5Vector(
            random(
                40, 100), random(
                40, 100), random(
                40, 100))

        # cube composed of 6 quads
        # Vertices of the cube
        self.vertices = []
        # front
        self.vertices.append(
            Py5Vector(-self.width / 2, -self.height / 2, self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2, -self.height / 2, self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2,
                self.height / 2,
                self.depth / 2))
        self.vertices.append(
            Py5Vector(-self.width / 2, self.height / 2, self.depth / 2))
        # left
        self.vertices.append(
            Py5Vector(-self.width / 2, -self.height / 2, self.depth / 2))
        self.vertices.append(
            Py5Vector(-self.width / 2, -self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(-self.width / 2, self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(-self.width / 2, self.height / 2, self.depth / 2))
        # right
        self.vertices.append(
            Py5Vector(
                self.width / 2, -self.height / 2, self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2, -self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2, self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2,
                self.height / 2,
                self.depth / 2))
        # back
        self.vertices.append(
            Py5Vector(-self.width / 2, -self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2, -self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2, self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(-self.width / 2, self.height / 2, -self.depth / 2))
        # top
        self.vertices.append(
            Py5Vector(-self.width / 2, -self.height / 2, self.depth / 2))
        self.vertices.append(
            Py5Vector(-self.width / 2, -self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2, -self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2, -self.height / 2, self.depth / 2))
        # bottom
        self.vertices.append(
            Py5Vector(-self.width / 2, self.height / 2, self.depth / 2))
        self.vertices.append(
            Py5Vector(-self.width / 2, self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2, self.height / 2, -self.depth / 2))
        self.vertices.append(
            Py5Vector(
                self.width / 2,
                self.height / 2,
                self.depth / 2))

    # Cube shape itself
    def draw_cube(self):
        # Draw cube
        for i in range(6):
            fill(self._quad_bg[i])
            begin_shape(QUADS)
            for j in range(4):
                vertex(self.vertices[j + 4 * i].x,
                       self.vertices[j + 4 * i].y,
                       self.vertices[j + 4 * i].z)
            end_shape()

    # Update location
    def update(self, bounds):
        self.position += self.velocity

        # Check wall collisions
        if self.position.x > bounds / 2 or self.position.x < -bounds / 2:
            self.velocity.x *= -1
        if self.position.y > bounds / 2 or self.position.y < -bounds / 2:
            self.velocity.y *= -1
        if self.position.z > bounds / 2 or self.position.z < -bounds / 2:
            self.velocity.z *= -1

    # Display method
    def display(self):
        with push_matrix():
            translate(self.position.x, self.position.y, self.position.z)
            rotate_x(frame_count * PI / self.rotation.x)
            rotate_y(frame_count * PI / self.rotation.y)
            rotate_z(frame_count * PI / self.rotation.z)
            no_stroke()
            self.draw_cube()  # Farm out shape to another method
