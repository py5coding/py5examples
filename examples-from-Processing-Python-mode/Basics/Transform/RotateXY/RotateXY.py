"""
Rotate 1.

Rotating simultaneously in the X and Y axis.
Transformation functions such as rotate() are additive.
Successively calling rotate(1.0) and rotate(2.0)
is equivalent to calling rotate(3.0).
"""

a = 0.0


def setup():
    size(640, 360, P3D)
    global r_size
    r_size = width / 6
    no_stroke()
    fill(204, 204)


def draw():
    global a
    background(126)

    a += 0.005
    if a > TWO_PI:
        a = 0.0

    translate(width / 2, height / 2)

    rotate_x(a)
    rotate_y(a * 2.0)
    fill(255)
    rect(-r_size, -r_size, r_size * 2, r_size * 2)

    rotate_x(a * 1.001)
    rotate_y(a * 2.002)
    fill(0)
    rect(-r_size, -r_size, r_size * 2, r_size * 2)
