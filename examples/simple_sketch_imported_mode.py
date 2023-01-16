"""
This is a simple sketch example written in imported mode.

You can run it from the command line like this:

$ run_sketch simple_sketch_module_mode.py

Or, you can run it in Thonny with the py5 Thonny plugin.

To setup Thonny with the py5 plugin, look here:

https://pypi.org/project/thonny-py5mode/

To learn more about the py5 modes, go here:

https://py5coding.org/content/py5_modes.html
"""

def setup():
    size(500, 500)
    background(196)
    color_mode(HSB, 360, 100, 100)


def draw():
    rand_x = random_int(width)
    rand_y = random_int(height)
    rand_hue = random(360)

    fill(rand_hue, 80, 80)
    square(rand_x, rand_y, 25)
