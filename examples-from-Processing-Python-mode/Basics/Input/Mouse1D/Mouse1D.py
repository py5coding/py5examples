"""
Mouse 1_d.

Move the mouse left and right to shift the balance.
The "mouseX" variable is used to control both the
size and color of the rectangles.
"""


def setup():
    size(640, 360)
    no_stroke()
    color_mode(RGB, height, height, height)
    rect_mode(CENTER)


def draw():
    background(0.0)

    r1 = map(mouse_x, 0, width, 0, height)
    r2 = height - r1

    fill(r1)
    rect(width / 2 + r1 / 2, height / 2, r1, r1)

    fill(r2)
    rect(width / 2 - r2 / 2, height / 2, r2, r2)
