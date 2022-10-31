"""
Texture Quad.

Load an image and draw it onto a quad. The texture() function sets
the texture image. The vertex() function maps the image to the geometry.
"""

half_width = None
half_height = None
img = None


def setup():
    global img, half_width, half_height
    size(640, 360, P3D)
    half_width = width / 2.0
    half_height = height / 2.0
    img = load_image("berlin-1.jpg")
    no_stroke()


def draw():
    background(0)

    translate(half_width, half_height)
    rotate_y(map(mouse_x, 0, width, -PI, PI))
    rotate_z(PI / 6)

    with begin_shape():
        texture(img)
        vertex(-100, -100, 0, 0, 0)
        vertex(100, -100, 0, img.width, 0)
        vertex(100, 100, 0, img.width, img.height)
        vertex(-100, 100, 0, 0, img.height)
