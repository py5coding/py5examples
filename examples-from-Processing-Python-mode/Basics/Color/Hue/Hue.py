"""
Hue.

Hue is the color reflected from or transmitted through an object
and is typically referred to as the name of the color (red, blue, yellow, etc.)
Move the cursor vertically over each bar to alter its hue.
"""

bar_width = 20


def setup():
    size(32 * bar_width, 360)
    color_mode(HSB, height, height, height)
    no_stroke()
    background(0)


def draw():
    which_bar = mouse_x / bar_width
    bar_x = which_bar * bar_width
    fill(mouse_y, height, height)
    rect(bar_x, 0, bar_width, height)
    last_bar = which_bar
