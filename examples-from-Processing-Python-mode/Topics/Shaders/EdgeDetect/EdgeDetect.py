"""
Edge Detection

Change the default shader to apply a simple, custom edge detection filter.

Press the mouse to switch between the custom and default shader.
"""
edges = None
img = None
enabled = True


def setup():
    global img, edges, enabled
    size(640, 360, P2D)
    img = load_image("leaves.jpg")
    edges = load_shader("edges.glsl")


def draw():
    if enabled:
        shader(edges)
    image(img, 0, 0)


def mouse_pressed():
    global enabled
    enabled = not enabled
    if not enabled:
        reset_shader()
