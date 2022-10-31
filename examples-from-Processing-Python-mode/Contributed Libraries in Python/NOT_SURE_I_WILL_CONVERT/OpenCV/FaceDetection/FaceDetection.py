add_library('opencv_processing')

opencv = OpenCV(this, "test.jpg")

size(opencv.width, opencv.height)

opencv.load_cascade(OpenCV.CASCADE_FRONTALFACE)
faces = opencv.detect()

image(opencv.get_input(), 0, 0)
no_fill()
stroke(0, 255, 0)
stroke_weight(3)
for i in range(len(faces)):
    rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height)
