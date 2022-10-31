"""
PolygonPShapeOOP.

Wrapping a Py5Shape inside a custom class
and demonstrating how we can have a multiple objects each
using the same PShape.
"""

import random
from polygon import Polygon

# A list of objects
polygons = []
# Three possible shapes
shapes = [None] * 3


def setup():
    size(640, 360, P2D)
    smooth()
    shapes[0] = create_shape(ELLIPSE, 0, 0, 100, 100)
    shapes[0].set_fill(color(255, 127))
    shapes[0].set_stroke(False)
    shapes[1] = create_shape(RECT, 0, 0, 100, 100)
    shapes[1].set_fill(color(255, 127))
    shapes[1].set_stroke(False)
    shapes[2] = create_shape()
    shapes[2].begin_shape()
    shapes[2].fill(0, 127)
    shapes[2].no_stroke()
    shapes[2].vertex(0, -50)
    shapes[2].vertex(14, -20)
    shapes[2].vertex(47, -15)
    shapes[2].vertex(23, 7)
    shapes[2].vertex(29, 40)
    shapes[2].vertex(0, 25)
    shapes[2].vertex(-29, 40)
    shapes[2].vertex(-23, 7)
    shapes[2].vertex(-47, -15)
    shapes[2].vertex(-14, -20)
    shapes[2].end_shape(CLOSE)

    for i in range(25):
        polygons.append(Polygon(random.choice(shapes)))


def draw():
    background(102)
    # Display and move them all.
    for poly in polygons:
        poly.display()
        poly.move()
