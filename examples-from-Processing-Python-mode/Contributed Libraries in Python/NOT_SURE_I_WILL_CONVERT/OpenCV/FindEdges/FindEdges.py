add_library('opencv_processing')

src = load_image("test.jpg")
size(src.width, src.height, P2D)

opencv = OpenCV(this, src)
opencv.find_canny_edges(20, 75)
canny = opencv.get_snapshot()

opencv.load_image(src)
opencv.find_scharr_edges(OpenCV.HORIZONTAL)
scharr = opencv.get_snapshot()

opencv.load_image(src)
opencv.find_sobel_edges(1, 0)
sobel = opencv.get_snapshot()

with push_matrix():
    scale(0.5)
    image(src, 0, 0)
    image(canny, src.width, 0)
    image(scharr, 0, src.height)
    image(sobel, src.width, src.height)
text("Source", 10, 25)
text("Canny", src.width / 2 + 10, 25)
text("Scharr", 10, src.height / 2 + 25)
text("Sobel", src.width / 2 + 10, src.height / 2 + 25)
