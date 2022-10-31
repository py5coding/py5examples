add_library('opencv_processing')

src = load_image("checkerboard.jpg")
src.resize(500, 0)
size(src.width, src.height, P2D)
opencv = OpenCV(this, src)
opencv.gray()

corner_points = opencv.find_chessboard_corners(9, 6)

image(opencv.get_output(), 0, 0)
fill(255, 0, 0)
no_stroke()
for p in corner_points:
    ellipse(p.x, p.y, 5, 5)
