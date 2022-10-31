add_library('opencv_processing')

src = load_image("test.jpg")
size(src.width, src.height/2, P2D)
opencv = OpenCV(this, src)
opencv.gray()
opencv.threshold(70)
dst = opencv.get_output()
contours = opencv.find_contours()
print("found %d contours" % contours.size())

scale(0.5)
image(src, 0, 0)
image(dst, src.width, 0)
no_fill()
stroke_weight(3)

for contour in contours:
    stroke(0, 255, 0)
    contour.draw()

    stroke(255, 0, 0)
    with begin_shape():
        for point in contour.get_polygon_approximation().get_points():
            vertex(point.x, point.y)
