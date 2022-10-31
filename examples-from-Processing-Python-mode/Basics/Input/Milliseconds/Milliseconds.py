"""
Milliseconds.

A millisecond is 1/1000 of a second.
Processing keeps track of the number of milliseconds a program has run.
By modifying this number with the modulo(%) operator,
different patterns in time are created.
"""


def setup():
    global scale_factor
    size(640, 360)
    no_stroke()
    scale_factor = width // 20


def draw():
    for i in range(0, scale_factor, 1):
        color_mode(RGB, (i + 1) * scale_factor * 10)
        fill(millis() % ((i + 1) * scale_factor * 10))
        rect(i * scale_factor, 0, scale_factor, height)
