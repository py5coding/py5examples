"""
Pixel Array.

Click and drag the mouse up and down to control the signal and
press and hold any key to see the current pixel being read.
This program sequentially reads the color of every pixel of an image
and displays this color to fill the window.
"""

direction = 1
signal = 0.0


def setup():
    size(640, 360)
    no_fill()
    stroke(255)
    frame_rate(30)
    global img
    img = load_image("sea.jpg")


def draw():
    global signal, direction
    if signal > img.width * img.height - 1 or signal < 0:
        direction = direction * -1
    if mouse_pressed:
        mx = constrain(mouse_x, 0, img.width - 1)
        my = constrain(mouse_y, 0, img.height - 1)
        signal = my * img.width + mx
    else:
        signal += 0.33 * direction
    sx = int(signal) % img.width
    sy = int(signal) / img.width
    if key_pressed:
        set(0, 0, img)  # fast way to draw an image
        point(sx, sy)
        rect(sx - 5, sy - 5, 10, 10)
    else:
        c = img.get(sx, sy)
        background(c)
