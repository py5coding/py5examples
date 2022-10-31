"""
Press 'w' to start/stop wiggling, space to restore original positions.
"""

cube_size = 320
circle_rad = 100
circle_res = 40
noise_mag = 1

wiggling = False


def setup():
    size(1024, 768, P3D)
    create_cube()


def draw():
    background(0)
    translate(width / 2, height / 2)
    rotate_x(frame_count * 0.01)
    rotate_y(frame_count * 0.01)
    shape(cube)

    if wiggling:
        pos = None
        for i in range(cube.get_child_count()):
            face = cube.get_child(i)
            for j in range(face.get_vertex_count()):
                pos = face.get_vertex(j, pos)
                pos.x += random(-noise_mag / 2.0, +noise_mag / 2.0)
                pos.y += random(-noise_mag / 2.0, +noise_mag / 2.0)
                pos.z += random(-noise_mag / 2.0, +noise_mag / 2.0)
                face.set_vertex(j, pos.x, pos.y, pos.z)

    if frame_count % 60 == 0:
        print(get_frame_rate())


def key_pressed():
    global wiggling
    if key == 'w':
        wiggling = not wiggling
    elif key == ' ':
        restore_cube()
    elif key == '1':
        cube.set_stroke_weight(1)
    elif key == '2':
        cube.set_stroke_weight(5)
    elif key == '3':
        cube.set_stroke_weight(10)


def create_cube():
    global cube
    cube = create_shape(GROUP)
    # Create all faces at front position
    for _ in range(6):
        face = create_shape()
        create_face_with_hole(face)
        cube.add_child(face)
    # Rotate all the faces to their positions
    # Front face - already correct
    face = cube.get_child(0)
    # Back face
    face = cube.get_child(1)
    face.rotate_y(radians(180))
    # Right face
    face = cube.get_child(2)
    face.rotate_y(radians(90))
    # Left face
    face = cube.get_child(3)
    face.rotate_y(radians(-90))
    # Top face
    face = cube.get_child(4)
    face.rotate_x(radians(90))
    # Bottom face
    face = cube.get_child(5)
    face.rotate_x(radians(-90))


def create_face_with_hole(face):
    face.begin_shape(POLYGON)
    face.stroke(255, 0, 0)
    face.fill(255)
    # Draw main shape Clockwise
    face.vertex(-cube_size / 2, -cube_size / 2, +cube_size / 2)
    face.vertex(+cube_size / 2, -cube_size / 2, +cube_size / 2)
    face.vertex(+cube_size / 2, +cube_size / 2, +cube_size / 2)
    face.vertex(-cube_size / 2, +cube_size / 2, +cube_size / 2)
    # Draw contour (hole) Counter-Clockwise
    face.begin_contour()
    for i in range(circle_res):
        angle = TWO_PI * i / circle_res
        x = circle_rad * sin(angle)
        y = circle_rad * cos(angle)
        z = +cube_size / 2
        face.vertex(x, y, z)
    face.end_contour()
    face.end_shape(CLOSE)


def restore_cube():
    # Rotation of faces is preserved, we just reset them the same way
    # as the "front" face and they will stay rotated correctly.
    for i in range(6):
        face = cube.get_child(i)
        restore_face_with_hole(face)


def restore_face_with_hole(face):
    face.set_vertex(0, -cube_size / 2, -cube_size / 2, +cube_size / 2)
    face.set_vertex(1, +cube_size / 2, -cube_size / 2, +cube_size / 2)
    face.set_vertex(2, +cube_size / 2, +cube_size / 2, +cube_size / 2)
    face.set_vertex(3, -cube_size / 2, +cube_size / 2, +cube_size / 2)
    for i in range(circle_res):
        angle = TWO_PI * i / circle_res
        x = circle_rad * sin(angle)
        y = circle_rad * cos(angle)
        z = +cube_size / 2
        face.set_vertex(4 + i, x, y, z)
