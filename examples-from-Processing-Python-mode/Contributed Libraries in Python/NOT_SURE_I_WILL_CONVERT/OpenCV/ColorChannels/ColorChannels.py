add_library('opencv_processing')

src = load_image("green_object.png")
src.resize(800, 0)
opencv = OpenCV(this, src)
size(int(opencv.width*1.5), int(opencv.height * 1.5), P2D)

img_h = src.height/2
img_w = src.width/2

r = opencv.get_snapshot(opencv.get_r())
g = opencv.get_snapshot(opencv.get_g())
b = opencv.get_snapshot(opencv.get_b())

opencv.use_color(HSB)

h = opencv.get_snapshot(opencv.get_h())
s = opencv.get_snapshot(opencv.get_s())
v = opencv.get_snapshot(opencv.get_v())

background(0)
no_tint()
image(src, img_w, 0, img_w, img_h)

tint(255, 0, 0)
image(r, 0, img_h, img_w, img_h)

tint(0, 255, 0)
image(g, img_w, img_h, img_w, img_h)

tint(0, 0, 255)
image(b, 2*img_w, img_h, img_w, img_h)

no_tint()
image(h, 0, 2*img_h, img_w, img_h)
image(s, img_w, 2*img_h, img_w, img_h)
image(v, 2*img_w, 2*img_h, img_w, img_h)
