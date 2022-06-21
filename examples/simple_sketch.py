def setup():
    size(500, 500)
    background(196)
    color_mode(HSB, 360, 100, 100)


def draw():
    rand_x = random_int(width)
    rand_y = random_int(height)
    rand_hue = random(360)

    fill(rand_hue, 80, 80)
    square(rand_x, rand_y, 25)

