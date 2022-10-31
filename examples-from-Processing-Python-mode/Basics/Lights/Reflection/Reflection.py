"""
Reflection
by Simon Greenwold.

Vary the specular reflection component of a material
with the horizontal position of the mouse.
"""


def setup():
    size(640, 360, P3D)
    no_stroke()
    color_mode(RGB, 1)
    fill(0.4)


def draw():
    background(0)
    translate(width / 2, height / 2)
    # Set the specular color of lights that follow
    light_specular(1, 1, 1)
    directional_light(0.8, 0.8, 0.8, 0, 0, -1)
    s = mouse_x / float(width)
    specular(s, s, s)
    sphere(120)
