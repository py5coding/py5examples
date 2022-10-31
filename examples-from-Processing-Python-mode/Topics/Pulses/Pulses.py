"""
Pulses.

Software drawing instruments can follow a rhythm or abide by rules independent
of drawn gestures. This is a form of collaborative drawing in which the draftsperson
controls some aspects of the image and the software controls others.
"""

offset = 0


def setup():
    size(640, 360)
    background(102)
    no_stroke()
    fill(0, 102)


def draw():
    global offset
    # Draw only when mouse is pressed
    if mouse_pressed:
        offset += 5
        radius = cos(radians(offset)) * 12.0
        for angle in range(0, 360, 75):
            x_off = cos(radians(angle)) * radius
            y_off = sin(radians(angle)) * radius
            fill(0)
            ellipse(mouse_x + x_off, mouse_y + y_off, radius, radius)
        fill(255)
        ellipse(mouse_x, mouse_y, 2, 2)
