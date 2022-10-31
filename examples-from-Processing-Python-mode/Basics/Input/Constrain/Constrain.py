"""
Constrain.

Move the mouse across the screen to move the circle.
The program constrains the circle to its box.
"""

mx = 0
my = 0
easing = 0.05
radius = 24
edge = 100
inner = edge + radius


def setup():
    size(640, 360)
    no_stroke()
    ellipse_mode(RADIUS)
    rect_mode(CORNERS)


def draw():
    global mx, my

    background(51)

    if abs(mouse_x - mx) > 0.1:
        mx = mx + (mouse_x - mx) * easing
    if abs(mouse_y - my) > 0.1:
        my = my + (mouse_y - my) * easing
    mx = constrain(mx, inner, width - inner)
    my = constrain(my, inner, height - inner)
    fill(76)
    rect(edge, edge, width - edge, height - edge)
    fill(255)
    ellipse(mx, my, radius, radius)
