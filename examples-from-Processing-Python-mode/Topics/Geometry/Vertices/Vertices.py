"""
Vertices
by Simon Greenwold.

Draw a cylinder centered on the y - axis, going down from y = 0 to y = height.
The radius at the top can be different from the radius at the bottom, and the
number of sides drawn is variable.
"""


def setup():
    global half_width, half_height
    size(640, 360, P3D)
    half_width = width / 2
    half_height = height / 2


def draw():
    background(0)
    lights()
    translate(half_width, half_height)
    rotate_y(map(mouse_x, 0, width, 0, PI))
    rotate_z(map(mouse_y, 0, height, 0, -PI))
    no_stroke()
    fill(255, 255, 255)
    translate(0, -40, 0)
    # Draw a mix between a cylinder and a cone.
    draw_cylinder(10, 180, 200, 16)
    # Draw a cylinder.
    # drawCylinder(70, 70, 120, 64)
    # Draw a pyramid.
    # drawCylinder(0, 180, 200, 4)


def draw_cylinder(top_radius, bottom_radius, tall, sides):
    angle = 0
    angle_increment = TAU / sides

    with begin_shape(QUAD_STRIP):
        for _ in range(sides + 1):
            vertex(top_radius * cos(angle), 0, top_radius * sin(angle))
            vertex(
                bottom_radius *
                cos(angle),
                tall,
                bottom_radius *
                sin(angle))
            angle += angle_increment

    # If it is not a cone, draw the circular top cap.
    if top_radius != 0:
        angle = 0
        with begin_shape(TRIANGLE_FAN):
            # Center point.
            vertex(0, 0, 0)
            for _ in range(sides + 1):
                vertex(top_radius * cos(angle), 0, top_radius * sin(angle))
                angle += angle_increment

    # If it is not a cone, draw the circular bottom cap.
    if bottom_radius != 0:
        angle = 0
        with begin_shape(TRIANGLE_FAN):
            # Center point.
            vertex(0, tall, 0)
            for _ in range(sides + 1):
                vertex(
                    bottom_radius *
                    cos(angle),
                    tall,
                    bottom_radius *
                    sin(angle))
                angle += angle_increment
