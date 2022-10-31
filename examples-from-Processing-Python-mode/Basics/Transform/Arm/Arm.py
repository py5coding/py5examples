"""
Arm.

The angle of each segment is controlled with the mouse_x and
mouse_y position. The transformations applied to the first segment
are also applied to the second segment because they are inside
the same push_matrix() and pop_matrix() group.
"""

seg_length = 100


def setup():
    size(600, 600)
    stroke_weight(30)
    stroke(255, 160)
    global x, y
    x = width * 0.3
    y = height * 0.5


def draw():
    background(0)

    angle1 = (mouse_x / float(width) - 0.5) * -PI
    angle2 = (mouse_y / float(height) - 0.5) * PI

    with push_matrix():
        segment(x, y, angle1)
        segment(seg_length, 0, angle2)


def segment(x, y, a):
    translate(x, y)
    rotate(a)
    line(0, 0, seg_length, 0)
