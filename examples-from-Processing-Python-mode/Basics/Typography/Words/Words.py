"""
 * Words.
 *
 * The text() function is used for writing words to the screen.
 * The letters can be aligned left, center, or right with the
 * text_align() function.
 """


def setup():
    size(640, 360)

    # Create the font
    print('\n'.join(Py5Font.list()))
    f = create_font("Georgia", 24)
    text_font(f)


def draw():
    background(102)
    text_align(RIGHT)
    draw_type(width * 0.25)
    text_align(CENTER)
    draw_type(width * 0.5)
    text_align(LEFT)
    draw_type(width * 0.75)


def draw_type(x):
    line(x, 0, x, 65)
    line(x, 220, x, height)
    fill(0)
    text("ichi", x, 95)
    fill(51)
    text("ni", x, 130)
    fill(204)
    text("san", x, 165)
    fill(255)
    text("shi", x, 210)
