"""
This is the simple_sketch.py code written for thonny from here:
https://github.com/py5coding/py5examples/blob/main/examples/simple_sketch.py
modified to Module Mode.
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
