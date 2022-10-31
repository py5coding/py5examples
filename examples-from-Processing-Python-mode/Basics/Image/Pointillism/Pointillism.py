"""
 * Pointillism
 * by Daniel Shiffman.
 *
 * Mouse horizontal location controls size of dots.
 * Creates a simple pointillist effect using ellipses colored
 * according to pixels in an image.
 """

small_point = 4
large_point = 40


def setup():
    size(640, 360)
    global img
    img = load_image("moonwalk.jpg")
    image_mode(CENTER)
    no_stroke()
    background(255)


def draw():
    pointillize = map(mouse_x, 0, width, small_point, large_point)
    x = int(random(img.width))
    y = int(random(img.height))
    pix = img.get(x, y)
    fill(pix, 128)
    ellipse(x, y, pointillize, pointillize)
