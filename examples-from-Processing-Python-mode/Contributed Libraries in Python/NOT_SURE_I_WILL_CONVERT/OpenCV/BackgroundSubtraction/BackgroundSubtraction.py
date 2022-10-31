add_library('video')
add_library('opencv_processing')


video = None
opencv = None


def setup():
    size(720, 480, P2D)
    video = Movie(this, "street.mov")
    opencv = OpenCV(this, 720, 480)

    opencv.start_background_subtraction(5, 3, 0.5)

    video.loop()
    video.play()


def draw():
    image(video, 0, 0)
    opencv.load_image(video)

    opencv.update_background()

    opencv.dilate()
    opencv.erode()
    no_fill()
    stroke(255, 0, 0)
    stroke_weight(3)
    for contour in opencv.find_contours():
        contour.draw()


def movie_event(m):
    m.read()
