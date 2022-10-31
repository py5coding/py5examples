"""
Morph.

Changing one shape into another by interpolating vertices from one to another.
"""

# Two lists to store the vertices for two shapes.
# This example assumes that each shape will have the same
# number of vertices, i.e. the size of each list will be the same.
circle = []
square = []

# A list for a third set of vertices, the ones we will be drawing
# in the window.
morph = []

# This variable will control if we are morphing to a circle or square.
state = False


def setup():
    size(640, 360)
    stroke_weight(4)

    # Create a circle using vectors pointing from center.
    for angle in range(0, 360, 9):
        # Note we are not starting from 0 in order to match the
        # path of a circle.
        v = Py5Vector.from_heading(radians(angle - 135))
        v *= 100
        circle.append(v)

        # Let's fill our morph ArrayList with blank PVectors while we're at it.
        morph.append(Py5Vector())

    # A square is a bunch of vertices along straight lines.
    # Top of square.
    for x in range(-50, 50, 10):
        square.append(Py5Vector(x, -50))

    # Right side.
    for y in range(-50, 50, 10):
        square.append(Py5Vector(50, y))

    # Bottom.
    for x in range(50, -50, -10):
        square.append(Py5Vector(x, 50))

    # Left side.
    for y in range(50, -50, -10):
        square.append(Py5Vector(-50, y))


def draw():
    background(51)
    global state

    # Draw relative to center.
    translate(width / 2, height / 2)

    # We will keep how far the vertices are from their target.
    total_distance = 0

    # Look at each vertex
    for i in range(len(circle)):
        # Are we lerping to the circle or square?
        if state:
            v1 = circle[i]
        else:
            v1 = square[i]

        # Get the vertex we will draw.
        v2 = morph[i]

        # Lerp to the target
        v2.lerp(v1, 0.1)

        # Check how far we are from target.
        total_distance += PVector.dist(v1, v2)

    # If all the vertices are close, switch shape.
    if total_distance < 0.1:
        state = not state

    # Draw a polygon that makes up all the vertices
    begin_shape()
    no_fill()
    stroke(255)
    for vector in morph:
        vertex(vector.x, vector.y)
    end_shape(CLOSE)
