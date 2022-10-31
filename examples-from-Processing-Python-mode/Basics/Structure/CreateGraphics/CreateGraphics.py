"""
 * Create Graphics.
 *
 * The create_graphics() function creates an object from the Py5Graphics class
 * Py5Graphics is the main graphics and rendering context for Processing.
 * The begin_draw() method is necessary to prepare for drawing and end_draw() is
 * necessary to finish. Use this class if you need to draw into an off-screen
 * graphics buffer or to maintain two contexts with different properties.
"""


def setup():
    size(640, 360)
    global pg
    pg = create_graphics(400, 200)


def draw():
    fill(0, 12)
    rect(0, 0, width, height)
    fill(255)
    no_stroke()
    ellipse(mouse_x, mouse_y, 60, 60)

    pg.begin_draw()
    pg.background(51)
    pg.no_fill()
    pg.stroke(255)
    pg.ellipse(mouse_x - 120, mouse_y - 60, 60, 60)
    pg.end_draw()

    # Draw the offscreen buffer to the screen with image()
    image(pg, 120, 60)
