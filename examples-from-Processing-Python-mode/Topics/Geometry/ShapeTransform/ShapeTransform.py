"""
Shape Transform
by Ira Greenberg.

Illustrates the geometric relationship between Cube, Pyramid, Cone and
Cylinder 3D primitives.

Instructions:
Up Arrow - increases points
Down Arrow - decreases points
'p' key toggles between cube / pyramid
"""

angle_inc = PI / 300.0
pts = 4
radius = 99
is_pyramid = False
cylinder_length = 95


def setup():
    global half_width, half_height
    size(640, 360, P3D)
    no_stroke()
    half_width = width / 2
    half_height = height / 2


def draw():
    global cylinder_length
    background(170, 95, 95)
    lights()
    fill(255, 200, 200)
    translate(half_width, half_height)
    rotate_x(frame_count * angle_inc)
    rotate_y(frame_count * angle_inc)
    rotate_z(frame_count * angle_inc)

    # Initialize vertex arrays.
    vertices = [[Py5Vector() for _ in range(pts + 1)] for _ in range(2)]

    # Fill arrays.
    for i in range(2):
        angle = 0
        for j in range(pts + 1):
            vertices[i][j].x = cos(radians(angle)) * radius
            vertices[i][j].y = sin(radians(angle)) * radius
            vertices[i][j].z = cylinder_length
            # Make the Pyramid point.
            if is_pyramid and i == 1:
                vertices[i][j].x = 0
                vertices[i][j].y = 0
            # The .0 after the 360 is critical.
            angle += 360.0 / pts
        cylinder_length *= -1

    # Draw cylinder tube.
    begin_shape(QUAD_STRIP)
    for j in range(pts + 1):
        vertex(vertices[0][j].x, vertices[0][j].y, vertices[0][j].z)
        vertex(vertices[1][j].x, vertices[1][j].y, vertices[1][j].z)
    end_shape()

    # Draw cylinder ends.
    for i in range(2):
        with begin_closed_shape():
            for j in range(pts):
                vertex(vertices[i][j].x, vertices[i][j].y, vertices[i][j].z)


"""
 up / down arrow keys control polygon detail.
"""


def key_pressed():
    global pts, is_pyramid
    if key == CODED:
        # Pts.
        if key_code == UP and pts < 90:
            pts += 1
        elif key_code == DOWN and pts > 4:
            pts -= 1

    if key == 'p':
        is_pyramid = not is_pyramid
