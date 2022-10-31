"""
Mouse functions.

Click on the box and drag it across the screen.
"""

box_size = 75
over_box = False
locked = False
x_offset = 0.0
y_offset = 0.0


def setup():
    size(640, 360)
    global bx, by
    bx = width / 2.0
    by = height / 2.0
    rect_mode(RADIUS)


def draw():
    global over_box

    background(0)
    if bx - box_size < mouse_x < bx + box_size and \
       by - box_size < mouse_y < by + box_size:
        over_box = True
        if not locked:
            stroke(255)
            fill(153)
    else:
        stroke(153)
        fill(153)
        over_box = False
    rect(bx, by, box_size, box_size)


def mouse_pressed():
    global locked, x_offset, y_offset
    if over_box:
        locked = True
        fill(255, 255, 255)
    else:
        locked = False
    x_offset = mouse_x - bx
    y_offset = mouse_y - by


def mouse_dragged():
    global bx, by

    if locked:
        bx = mouse_x - x_offset
        by = mouse_y - y_offset


def mouse_released():
    global locked
    locked = False
