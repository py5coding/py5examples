"""
Easing.

Move the mouse across the screen and the symbol will follow.
Between drawing each frame of the animation, the program
calculates the difference between the position of the
symbol and the cursor. If the distance is larger than
1 pixel, the symbol moves part of the distance (0.05) from its
current position toward the cursor.
"""

x = 0
y = 0
easing = 0.05


def setup():
    size(640, 360)
    no_stroke()


def draw():
    global x, y

    background(51)

    target_x = mouse_x
    dx = target_x - x
    if(abs(dx) > 1):
        x += dx * easing

    target_y = mouse_y
    dy = target_y - y
    if(abs(dy) > 1):
        y += dy * easing

    ellipse(x, y, 66, 66)
