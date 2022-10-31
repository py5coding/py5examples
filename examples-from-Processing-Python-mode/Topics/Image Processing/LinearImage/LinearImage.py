"""
Linear Image.

Click and drag mouse up and down to control the signal.
Press and hold any key to watch the scanning.
"""
img = load_image("sea.jpg")
direction = 1
signal = 0.0


def setup():
    global img
    img = load_image("sea.jpg")
    size(640, 360)
    stroke(255)
    img.load_pixels()
    load_pixels()


def draw():
    global signal, direction
    if signal > img.height - 1 or signal < 0:
        direction = direction * -1
    if mouse_pressed:
        signal = abs(mouse_y % img.height)
    else:
        signal += (0.3 * direction)
    if key_pressed:
        set(0, 0, img)
        line(0, signal, img.width, signal)
    else:
        signal_offset = int(signal) * img.width
        for y in range(img.height):
            list_copy(img.pixels, signal_offset, pixels, y * width, img.width)
        update_pixels()


def list_copy(src, src_pos, dst, dst_pos, length):
    dst[dst_pos:dst_pos + length] = src[src_pos:src_pos + length]
