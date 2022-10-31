"""
Blending
by Andres Colubri.
Images can be blended using one of the 10 blending modes
(currently available only in P2D and P3).
Click to go to cycle through the modes.
"""

modes = ((REPLACE, "REPLACE"),
         (BLEND, "BLEND"),
         (ADD, "ADD"),
         (SUBTRACT, "SUBTRACT"),
         (LIGHTEST, "LIGHTEST"),
         (DARKEST, "DARKEST"),
         (DIFFERENCE, "DIFFERENCE"),
         (EXCLUSION, "EXCLUSION"),
         (MULTIPLY, "MULTIPLY"),
         (SCREEN, "SCREEN"),
         (REPLACE, "REPLACE"))

current_mode = 0


def setup():
    size(640, 360, P3D)
    no_stroke()
    global img1, img2
    img1 = load_image("layer1.jpg")
    img2 = load_image("layer2.jpg")


def draw():
    global pic_alpha
    sel_mode, name = modes[current_mode]
    pic_alpha = int(map(mouse_x, 0, width, 0, 255))
    background(0)
    tint(255, 255)
    image(img1, 0, 0)
    blend_mode(sel_mode)
    tint(255, pic_alpha)
    image(img2, 0, 0)
    blend_mode(REPLACE)
    fill(255)
    rect(0, 0, 94, 22)
    fill(0)
    text(name, 10, 15)


def mouse_pressed():
    global current_mode
    current_mode = (current_mode + 1) % len(modes)


def mouse_dragged():
    global pic_alpha
    if height - 50 < mouse_y:
        pic_alpha = int(map(mouse_x, 0, width, 0, 255))
