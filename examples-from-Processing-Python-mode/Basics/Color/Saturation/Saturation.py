"""
Saturation.

Saturation is the strength or purity of the color and represents the
amount of gray in proportion to the hue. A "saturated" color is pure
and an "unsaturated" color has a large percentage of gray.
Move the cursor vertically over each bar to alter its saturation.
"""

bar_width = 20


def setup():
    size(bar_width * 32, 360)
    color_mode(HSB, width, height, 100)
    no_stroke()


def draw():
    which_bar = mouse_x / bar_width
    bar_x = which_bar * bar_width
    fill(bar_x, mouse_y, 66)
    rect(bar_x, 0, bar_width, height)
