"""
Performance demo using text rendering
"""


def setup():
    size(800, 600, P2D)
    fill(0)


def draw():
    background(255)
    for i in range(10000):
        x = random(width)
        y = random(height)
        text("HELLO", x, y)

    if frame_count % 10 == 0:
        print(get_frame_rate())
