"""
Texture Triangle.

Using a rectangular image to map a texture onto a triangle.
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
    translate(half_width, half_height, 0)
    rotate_y(map(mouse_x, 0, width, -PI, PI))

    with begin_shape():
        texture(img)
        vertex(-100, -100, 0, 0, 0)
        vertex(100, -40, 0, 300, 120)
        vertex(0, 100, 0, 200, 400)
