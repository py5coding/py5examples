"""
Rollover.

Roll over the colored squares in the center of the image
to change the color of the outside rectangle.
"""

rect_size = 90  # Diameter of rect
circle_size = 93  # Diameter of circle
rect_color = color(0)
circle_color = color(255)
base_color = color(102)
rect_over = False
circle_over = False


def setup():
    size(640, 360)
    # Position of circle button
    global circle_x, circle_y
    circle_x = width / 2 + circle_size / 2 + 10
    circle_y = height / 2
    # Position of square button
    global rect_x, rect_y
    rect_x = width / 2 - rect_size - 10
    rect_y = height / 2 - rect_size / 2
    ellipse_mode(CENTER)


def draw():
    update(mouse_x, mouse_y)
    no_stroke()
    if rect_over:
        background(rect_color)
    elif circle_over:
        background(circle_color)
    else:
        background(base_color)
    stroke(255)
    fill(rect_color)
    rect(rect_x, rect_y, rect_size, rect_size)
    stroke(0)
    fill(circle_color)
    ellipse(circle_x, circle_y, circle_size, circle_size)


def update(x, y):
    global circle_over, rect_over
    circle_over = over_circle(circle_x, circle_y, circle_size)
    rect_over = over_rect(rect_x, rect_y, rect_size, rect_size)


def over_rect(x, y, width, height):
    return x <= mouse_x <= x + width and y <= mouse_y <= y + height


def over_circle(x, y, diameter):
    distance = dist(x, y, mouse_x, mouse_y)
    return distance < diameter / 2
