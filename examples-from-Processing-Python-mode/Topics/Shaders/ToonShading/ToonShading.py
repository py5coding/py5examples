"""
Toon Shading.

Example showing the use of a custom lighting shader in order
to apply a "toon" effect on the scene. Based on the glsl tutorial
from lighthouse 3D:
http://www.lighthouse3d.com/tutorials/glsl-tutorial/toon-shader-version-ii/
"""

toon = None
shader_enabled = True


def setup():
    global toon
    size(640, 360, P3D)
    no_stroke()
    fill(204)
    toon = load_shader("ToonFrag.glsl", "ToonVert.glsl")


def draw():
    if shader_enabled:
        shader(toon)
    no_stroke()
    background(0)
    dir_y = (mouse_y / float(height) - 0.5) * 2
    dir_x = (mouse_x / float(width) - 0.5) * 2
    directional_light(204, 204, 204, -dir_x, -dir_y, -1)
    translate(width / 2, height / 2)
    sphere(120)


def mouse_pressed():
    global shader_enabled
    shader_enabled = not shader_enabled
    if not shader_enabled:
        reset_shader()
