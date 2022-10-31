"""
PathPShape

A simple path using Py5Shape
"""


def setup():
    size(640, 360, P2D)
    smooth()
    # Create the shape.
    global path
    path = create_shape()
    path.begin_shape()
    # Set fill and stroke.
    path.no_fill()
    path.stroke(255)
    path.stroke_weight(2)
    x = 0
    # Calculate the path as a sine wave.
    for i in range(0, int(round(TWO_PI * 10)), 1):
        itemp = i * .1
        path.vertex(x, sin(itemp) * 100)
        x += 5
    # The path is complete.
    path.end_shape()


def draw():
    background(51)
    # Draw the path at the mouse location.
    translate(mouse_x, mouse_y)
    shape(path)
