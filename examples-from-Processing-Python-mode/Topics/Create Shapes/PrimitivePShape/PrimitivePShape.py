"""
PrimitivePShape.

Using a Py5Shape to display a primitive shape (in this case, ellipse).
"""


def setup():
    size(640, 360, P2D)
    smooth()
    # Creating the PShape as an ellipse.
    global circle
    circle = create_shape(ELLIPSE, 0, 0, 100, 50)


def draw():
    background(51)
    # We can dynamically set the stroke and fill of the shape.
    circle.set_stroke(color(255))
    circle.set_stroke_weight(4)
    circle.set_fill(color(map(mouse_x, 0, width, 0, 255)))
    # We can use translate to move the PShape.
    translate(mouse_x, mouse_y)
    # Drawing the PShape
    shape(circle)
