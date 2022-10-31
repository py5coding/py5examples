from org.opencv.imgproc import Imgproc
from org.opencv.core import Core, Mat, Point, Scalar, Size, CvType
add_library('opencv_processing')


def color_to_scalar(c):
    # in BGR
    return Scalar(blue(c), green(c), red(c))


src = load_image("test.jpg")
src.resize(src.width / 2, 0)
size(src.width * 2 + 256, src.height)
# third argument is: useColor
opencv = OpenCV(this, src, True)
skin_histogram = Mat.zeros(256, 256, CvType.CV_8UC1)
Core.ellipse(skin_histogram,
             Point(113.0, 155.6),
             Size(40.0, 25.2),
             43.0, 0.0, 360.0,
             Scalar(255, 255, 255), Core.FILLED)
hist_mask = create_image(256, 256, ARGB)
opencv.to_p_image(skin_histogram, hist_mask)
hist = load_image("cb-cr.png")
hist.blend(hist_mask, 0, 0, 256, 256, 0, 0, 256, 256, ADD)

dst = opencv.get_output()
dst.load_pixels()

for i in range(len(dst.pixels)):
    input = Mat(Size(1, 1), CvType.CV_8UC3)
    input.set_to(color_to_scalar(dst.pixels[i]))
    output = opencv.imitate(input)
    Imgproc.cvtColor(input, output, Imgproc.COLOR_BGR2YCrCb)
    input_components = output.get(0, 0)
    if skin_histogram.get(int(input_components[1]), int(
            input_components[2]))[0] > 0:
        dst.pixels[i] = color(255)
    else:
        dst.pixels[i] = color(0)

dst.update_pixels()

image(src, 0, 0)
image(dst, src.width, 0)
image(hist, src.width * 2, 0)
