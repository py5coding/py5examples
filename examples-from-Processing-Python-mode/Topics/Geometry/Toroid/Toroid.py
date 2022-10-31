"""
Interactive Toroid
by Ira Greenberg.

Illustrates the geometric relationship between Toroid, Sphere, and Helix
3D primitives, as well as lathing principal.

Instructions:
UP arrow key pts++
DOWN arrow key pts--
LEFT arrow key segments--
RIGHT arrow key segments++
'a' key toroid radius--
's' key toroid radius++
'z' key initial polygon radius--
'x' key initial polygon radius++
'w' key toggle wireframe / solid shading
'h' key toggle sphere / helix
"""

pts = 40
angle = 0.001
radius = 60.0

# Lathe segments.
segments = 60
lathe_radius = 100.0

# For shaded or wireframe rendering.
is_wire_frame = False

# For optional helix.
is_helix = False
helix_offset = 5.0
PIOneFifty = PI / 150
PIOneSeventy = PI / 170
PINinety = PI / 90


def setup():
    size(640, 360, P3D)
    global half_width, half_height
    half_width = width / 2
    half_height = height / 2


def draw():
    background(50, 64, 42)

    # Basic lighting setup.
    lights()

    # 2 rendering styles:
    # Wireframe...
    if is_wire_frame:
        stroke(255, 255, 150)
        no_fill()
    # ...or solid.
    else:
        no_stroke()
        fill(150, 195, 125)

    # Center and spin toroid.
    translate(half_width, half_height, -100)
    rotate_x(frame_count * PIOneFifty)
    rotate_y(frame_count * PIOneSeventy)
    rotate_z(frame_count * PINinety)

    vertices = [Py5Vector() for _ in range(pts + 1)]
    vertices2 = [Py5Vector() for _ in range(pts + 1)]

    # Fill arrays.
    global angle
    for i in range(pts + 1):
        # vertices
        vertices[i].x = lathe_radius + sin(radians(angle)) * radius
        vertices[i].z = cos(radians(angle)) * radius
        if is_helix:
            vertices[i].z -= helix_offset * segments / 2.0
        angle += 360.0 / pts

    # Draw toroid.
    lathe_angle = 0
    for i in range(segments + 1):
        begin_shape(QUAD_STRIP)
        for j in range(pts + 1):
            if i > 0:
                vertex(vertices2[j].x, vertices2[j].y, vertices2[j].z)
            vertices2[j].x = cos(radians(lathe_angle)) * vertices[j].x
            vertices2[j].y = sin(radians(lathe_angle)) * vertices[j].x
            vertices2[j].z = vertices[j].z
            # Optional helix offset.
            if is_helix:
                vertices[j].z += helix_offset
            vertex(vertices2[j].x, vertices2[j].y, vertices2[j].z)
        # Create extra rotation for helix.
        if is_helix:
            lathe_angle += 720.0 / segments
        else:
            lathe_angle += 360.0 / segments
        end_shape()


def key_pressed():
    global pts, segments, lathe_radius, radius, is_wire_frame, is_helix
    """
    left / right arrow keys control ellipse detail.
    up / down arrow keys control segment detail.
    'a', 's' keys control lathe radius.
    'z', 'x' keys control ellipse radius.
    'w' key toggles between wireframe and solid.
    'h' key toggles between toroid and helix.
    """
    if key == CODED:
        # Points.
        if key_code == UP and pts < 40:
            pts += 1
        elif key_code == DOWN and pts > 3:
            pts -= 1
        # Extrusion length.
        if key_code == LEFT and segments > 3:
            segments -= 1
        elif key_code == RIGHT and segments < 80:
            segments += 1

    # Lathe radius.
    if key == 'a' and lathe_radius > 0:
        lathe_radius -= 1
    elif key == 's':
        lathe_radius += 1

    # Ellipse radius.
    if key == 'z' and radius > 10:
        radius -= 1
    elif key == 'x':
        radius += 1

    # Wireframe.
    if key == 'w':
        is_wire_frame = not is_wire_frame

    # Helix.
    if key == 'h':
        is_helix = not is_helix
