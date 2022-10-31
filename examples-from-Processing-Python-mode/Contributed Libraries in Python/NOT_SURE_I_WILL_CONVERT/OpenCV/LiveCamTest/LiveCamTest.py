add_library('video')
add_library('opencv_processing')

video = None
opencv = None
show_fps = False


def setup():
    global opencv
    global video
    size(640, 480)
    video = Capture(this, 640 / 2, 480 / 2)
    opencv = OpenCV(this, 640 / 2, 480 / 2)
    opencv.load_cascade(OpenCV.CASCADE_FRONTALFACE)
    video.start()
    frame_rate(12)


def draw():
    scale(2)
    opencv.load_image(video)
    image(video, 0, 0)
    no_fill()
    stroke(0, 255, 0)
    stroke_weight(3)
    faces = opencv.detect()
    for face in faces:
        rect(face.x, face.y, face.width, face.height)
    if show_fps:
        text("%d fps" % get_frame_rate(), 20, 20)


def capture_event(c):
    c.read()


def mouse_pressed():
    global show_fps
    show_fps = not show_fps
