"""
Keyboard.

Click on the image to give it focus and press the letter keys
to create forms in time and space. Each key has a unique identifying
number. These numbers can be used to position shapes in space.
"""


def setup():
    size(640, 360)
    no_stroke()
    background(0)
    global rect_width
    rect_width = width / 4


def draw():
    # Keep draw() here to continue looping while waiting for keys
    pass


def key_pressed():
    key_index = -1
    if 'A' <= key <= 'Z':
        key_index = ord(key) - ord('A')
    elif 'a' <= key <= 'z':
        key_index = ord(key) - ord('a')
    if key_index == -1:
        # If it's not a letter key, clear the screen
        background(0)
    else:
        # It's a letter key, fill a rectangle
        fill(millis() % 255)
        x = map(key_index, 0, 25, 0, width - rect_width)
        rect(x, 0, rect_width, height)
