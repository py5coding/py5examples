"""
This is a simple sketch example written in module mode.

You can run it from the command line like this:

$ python simple_sketch_module_mode.py

To learn more about the py5 modes, go here:

https://py5coding.org/content/py5_modes.html
"""

import py5


def setup():
    py5.size(500, 500)
    py5.background(196)
    py5.color_mode(py5.HSB, 360, 100, 100)


def draw():
    rand_x = py5.random_int(py5.width)
    rand_y = py5.random_int(py5.height)
    rand_hue = py5.random(360)

    py5.fill(rand_hue, 80, 80)
    py5.square(rand_x, rand_y, 25)


py5.run_sketch()
