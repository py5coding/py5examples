'''
    A wireframe box with colored edges which expands and contracts according
    to time-of-day.
    An original implementation of *hms* from http://www.gysin-vanetti.com/hms
    (C) Ben Alkov, 2014, licensed as APL 2.0 as part of processing.py
    (https://github.com/jdf/processing.py).
'''


def setup():
    global fill_cube, edge_cube
    size(500, 500, P3D)
    smooth(4)
    camera(0, 0, 100,
           0, 0, 0,
           0, 1, 0)

    # Creating a **filled** wireframe cube is non-obvious.
    # We need an opaque black cube inside a transparent wireframe cube.
    fill_cube = create_shape(BOX, 2)
    edge_cube = make_edge_cube()

    # The fill color here has to match the `background` from `draw` in order
    # for the fill cube to be invisible.
    fill_cube.set_fill(color(10))


def draw():
    rotate_x(sin(frame_count * 0.008))
    rotate_y(cos(frame_count * 0.008))

    # The fill color here has to match the `fillCube`'s `setFill` color in
    # order for the fill cube to be invisible.
    background(10)
    draw_shape()


def draw_shape():
    # `map`; "Re-maps a number from one range to another."
    # Scale time units to 3D coordinates.
    x = remap(second(), 0, 59, 1, 12)
    y = remap(minute(), 0, 59, 1, 12)
    z = remap(hour(), 0, 23, 1, 12)

    scale(x, y, z)
    shape(fill_cube, 0, 0)
    shape(edge_cube, 0, 0)


def make_edge_cube():
    # Draw a 2x2x2 transparent cube with edges colored according to the
    # current time.
    Red = color(255, 137, 95)  # Seconds.
    Green = color(176, 255, 121)  # Minutes.
    Blue = color(56, 76, 204)  # Hours.
    edge_cube = create_shape()
    edge_cube.begin_shape(LINES)

    # Seconds - lines along `x`.
    edge_cube.stroke(Red)
    edge_cube.vertex(-1, 1, 1)
    edge_cube.vertex(1, 1, 1)
    edge_cube.vertex(-1, -1, 1)
    edge_cube.vertex(1, -1, 1)
    edge_cube.vertex(-1, -1, -1)
    edge_cube.vertex(1, -1, -1)
    edge_cube.vertex(-1, 1, -1)
    edge_cube.vertex(1, 1, -1)

    # Minutes - lines along `y`.
    edge_cube.stroke(Green)
    edge_cube.vertex(-1, 1, 1)
    edge_cube.vertex(-1, -1, 1)
    edge_cube.vertex(1, 1, 1)
    edge_cube.vertex(1, -1, 1)
    edge_cube.vertex(1, 1, -1)
    edge_cube.vertex(1, -1, -1)
    edge_cube.vertex(-1, 1, -1)
    edge_cube.vertex(-1, -1, -1)

    # Hours - lines along `z`.
    edge_cube.stroke(Blue)
    edge_cube.vertex(-1, 1, -1)
    edge_cube.vertex(-1, 1, 1)
    edge_cube.vertex(1, 1, -1)
    edge_cube.vertex(1, 1, 1)
    edge_cube.vertex(1, -1, -1)
    edge_cube.vertex(1, -1, 1)
    edge_cube.vertex(-1, -1, -1)
    edge_cube.vertex(-1, -1, 1)
    edge_cube.end_shape()
    return edge_cube
