add_library('opencv_processing')

img = None
opencv = None


def setup():
    img = load_image("test.jpg")
    size(img.width, img.height, P2D)
    opencv = OpenCV(this, img)


def draw():
    opencv.load_image(img)
    opencv.brightness(int(map(mouse_x, 0, width, -255, 255)))
    image(opencv.get_output(), 0, 0)
