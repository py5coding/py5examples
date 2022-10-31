"""
Texture Cylinder.

Load an image and draw it onto a cylinder and a quad.
"""

half_width = None
half_height = None
tube_res = 32
tube_x = [0.0 for _ in range(tube_res)]
tube_y = [0.0 for _ in range(tube_res)]
img = None


def setup():
    size(640, 360, P3D)
    global half_width, half_height, img
    half_width = width / 2.0
    half_height = height / 2.0
    img = load_image("berlin-1.jpg")
    angle = 270.0 / tube_res
    for i in range(tube_res):
        tube_x[i] = cos(radians(i * angle))
        tube_y[i] = sin(radians(i * angle))
    no_stroke()


def draw():
    background(0)

    translate(half_width, half_height)
    rotate_x(map(mouse_y, 0, height, -PI, PI))
    rotate_y(map(mouse_x, 0, width, -PI, PI))

    begin_shape(QUAD_STRIP)
    texture(img)
    for i in range(tube_res):
        x = tube_x[i] * 100
        z = tube_y[i] * 100
        u = img.width / tube_res * i
        vertex(x, -100, z, u, 0)
        vertex(x, 100, z, u, img.height)
    end_shape()

    with begin_shape(QUADS):
        texture(img)
        vertex(0, -100, 0, 0, 0)
        vertex(100, -100, 0, 100, 0)
        vertex(100, 100, 0, 100, 100)
        vertex(0, 100, 0, 0, 100)
