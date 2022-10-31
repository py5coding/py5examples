"""
Zoom.

Move the cursor over the image to alter its position. Click and press
the mouse to zoom. This program displays a series of lines with their
heights corresponding to a color value read from an image.
"""

scale_val = 1.0
nmx = 0
nmy = 0
res = 5


def setup():
    size(640, 360, P3D)
    no_fill()
    stroke(255)
    global img, img_pixels
    img = load_image("ystone08.jpg")
    img_pixels = [[0] * img.width for _ in range(img.height)]
    for i in range(img.height):
        for j in range(img.width):
            img_pixels[j][i] = img.get(j, i)


def draw():
    global nmx, nmy, scale_val
    background(0)
    nmx += (mouse_x - nmx) / 20
    nmy += (mouse_y - nmy) / 20
    if mouse_pressed:
        scale_val += 0.005
    else:
        scale_val -= 0.01
    scale_val = constrain(scale_val, 1.0, 2.0)
    translate(width / 2 + nmx * scale_val - 100,
              height / 2 + nmy * scale_val - 100, -50)
    scale(scale_val)
    rotate_z(PI / 9 - scale_val + 1.0)
    rotate_x(PI / scale_val / 8 - 0.125)
    rotate_y(scale_val / 8 - 0.125)
    translate(-width / 2, -height / 2, 0)
    for i in range(0, img.height, res):
        for j in range(0, img.width, res):
            rr = red(img_pixels[j][i])
            gg = green(img_pixels[j][i])
            bb = blue(img_pixels[j][i])
            tt = rr + gg + bb
            stroke(rr, gg, gg)
            line(i, j, tt / 10 - 20, i, j, tt / 10)
