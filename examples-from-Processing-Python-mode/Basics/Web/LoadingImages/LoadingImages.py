"""
Loading Images.
"""


def setup():
    size(640, 360)
    global img
    img = load_image("http://processing.org/img/processing-web.png")
    no_loop()


def draw():
    background(0)
    for i in range(5):
        image(img, 0, img.height * i)
