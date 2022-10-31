"""
Relativity.

Each color is perceived in relation to other colors. The top and bottom
bars each contain the same component colors, but a different display order
causes individual colors to appear differently.
"""

a = color(165, 167, 20)
b = color(77, 86, 59)
c = color(42, 106, 105)
d = color(165, 89, 20)
e = color(146, 150, 127)


def setup():
    size(640, 360)
    no_stroke()
    no_loop()    # Draw only one time


def draw():
    draw_band(a, b, c, d, e, 0, width / 128)
    draw_band(c, a, d, b, e, height / 2, width / 128)


def draw_band(v, w, x, y, z, ypos, bar_width):
    num = 5
    color_order = (v, w, x, y, z)
    for i in range(0, width, bar_width * num):
        for j in range(num):
            fill(color_order[j])
            rect(i + j * bar_width, ypos, bar_width, height / 2)
