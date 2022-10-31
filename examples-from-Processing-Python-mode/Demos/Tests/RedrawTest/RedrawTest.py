def setup():
    size(400, 400, P3D)
    no_loop()


def draw():
    background(255, 0, 0)
    ellipse(mouse_x, mouse_y, 100, 50)
    print("draw")


def key_pressed():
    redraw()
