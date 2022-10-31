"""
Radial Gradient.

Draws a series of concentric circles to create a gradient
from one color to another.
"""


def setup():
    size(640, 360)
    background(0)
    color_mode(HSB, 360, 100, 100)
    no_stroke()
    ellipse_mode(RADIUS)
    frame_rate(1)


def draw():
    background(0)
    for x in range(0, width + 1, width / 2):
        draw_gradient(x, height / 2)


def draw_gradient(x, y):
    radius = width / 4
    h = random(0, 360)
    for r in range(radius, 0, -1):
        fill(h, 90, 90)
        ellipse(x, y, r, r)
        h = (h + 1) % 360
