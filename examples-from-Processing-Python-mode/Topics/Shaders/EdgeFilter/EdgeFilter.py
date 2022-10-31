"""
Edge Filter

Apply a custom shader to the filter() function to affect the geometry drawn to the screen.

Press the mouse to turn the filter on and off.
"""

edges = None
apply_filter = True


def setup():
    global edges
    size(640, 360, P3D)
    edges = load_shader("edges.glsl")
    no_stroke()


def draw():
    background(0)
    lights()
    translate(width / 2, height / 2)
    with push_matrix():
        rotate_x(frame_count * 0.01)
        rotate_y(frame_count * 0.01)
        box(120)
    if apply_filter:
        filter(edges)
    # The sphere doesn't have the edge detection applied
    # on it because it is drawn after filter() is called.
    rotate_y(frame_count * 0.02)
    translate(150, 0)
    sphere(40)


def mouse_pressed():
    global apply_filter
    apply_filter = not apply_filter
