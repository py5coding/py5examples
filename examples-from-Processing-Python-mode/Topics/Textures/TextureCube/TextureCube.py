"""
Texture Cube
by Dave Bollinger.

Drag mouse to rotate cube. Demonstrates use of u / v coords in vertex() and
effect on texture(). The textures get distorted using the P3D renderer as you
can see, but they look great using OPENGL.
"""

half_width = None
half_height = None
tex = None
rotx = PI / 4
roty = PI / 4


def setup():
    size(640, 360, P3D)
    global half_width, half_height, tex
    half_width = width / 2.0
    half_height = height / 2.0
    tex = load_image("berlin-1.jpg")
    texture_mode(NORMAL)
    fill(255)
    stroke(color(44, 48, 32))


def draw():
    background(0)
    no_stroke()

    translate(half_width, half_height, -100)
    rotate_x(rotx)
    rotate_y(roty)
    scale(90)

    textured_cube(tex)


def textured_cube(tex):
    with begin_shape(QUADS):
        texture(tex)

        # Given one texture and six faces, we can easily set up the uv coordinates
        # such that four of the faces tile "perfectly" along either u or v, but
        # the other two faces cannot be so aligned. This code tiles "along" u,
        # "around" the X / Z faces and fudges the Y faces - the Y faces are
        # arbitrarily aligned such that a rotation along the X axis will put the
        # "top" of either texture at the "top" of the screen, but is not
        # otherwised aligned with the X / Z faces. (This just affects what type of
        # symmetry is required if you need seamless tiling all the way around the
        # cube)

        # +Z "front" face.
        vertex(-1, -1, 1, 0, 0)
        vertex(1, -1, 1, 1, 0)
        vertex(1, 1, 1, 1, 1)
        vertex(-1, 1, 1, 0, 1)

        # -Z "back" face.
        vertex(1, -1, -1, 0, 0)
        vertex(-1, -1, -1, 1, 0)
        vertex(-1, 1, -1, 1, 1)
        vertex(1, 1, -1, 0, 1)

        # +Y "bottom" face.
        vertex(-1, 1, 1, 0, 0)
        vertex(1, 1, 1, 1, 0)
        vertex(1, 1, -1, 1, 1)
        vertex(-1, 1, -1, 0, 1)

        # -Y "top" face.
        vertex(-1, -1, -1, 0, 0)
        vertex(1, -1, -1, 1, 0)
        vertex(1, -1, 1, 1, 1)
        vertex(-1, -1, 1, 0, 1)

        # +X "right" face.
        vertex(1, -1, 1, 0, 0)
        vertex(1, -1, -1, 1, 0)
        vertex(1, 1, -1, 1, 1)
        vertex(1, 1, 1, 0, 1)

        # -X "left" face.
        vertex(-1, -1, -1, 0, 0)
        vertex(-1, -1, 1, 1, 0)
        vertex(-1, 1, 1, 1, 1)
        vertex(-1, 1, -1, 0, 1)


def mouse_dragged():
    global rotx, roty
    rate = 0.01
    rotx += (pmouse_y - mouse_y) * rate
    roty += (mouse_x - pmouse_x) * rate
