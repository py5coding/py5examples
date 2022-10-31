"""
Separate Blur Shader

This blur shader works by applying two successive passes, one horizontal
and the other vertical.

Press the mouse to switch between the custom and default shader.
"""
blur = None
src = None
pass1 = None
pass2 = None


def setup():
    global blur, src, pass1, pass2
    size(640, 360, P2D)

    blur = load_shader("blur.glsl")
    blur.set("blurSize", 9)
    blur.set("sigma", 5.0)

    src = create_graphics(width, height, P2D)

    pass1 = create_graphics(width, height, P2D)
    pass1.no_smooth()

    pass2 = create_graphics(width, height, P2D)
    pass2.no_smooth()


def draw():
    src.begin_draw()
    src.background(0)
    src.fill(255)
    src.ellipse(width / 2, height / 2, 100, 100)
    src.end_draw()

    # Applying the blur shader along the vertical direction
    blur.set("horizontalPass", 0)
    pass1.begin_draw()
    pass1.shader(blur)
    pass1.image(src, 0, 0)
    pass1.end_draw()

    # Applying the blur shader along the horizontal direction
    blur.set("horizontalPass", 1)
    pass2.begin_draw()
    pass2.shader(blur)
    pass2.image(pass1, 0, 0)
    pass2.end_draw()

    image(pass2, 0, 0)


def key_pressed():
    global blur
    if key == '9':
        blur.set("blurSize", 9)
        blur.set("sigma", 5.0)
    elif key == '7':
        blur.set("blurSize", 7)
        blur.set("sigma", 3.0)
    elif key == '5':
        blur.set("blurSize", 5)
        blur.set("sigma", 2.0)
    elif key == '3':
        blur.set("blurSize", 3)
        blur.set("sigma", 1.0)
