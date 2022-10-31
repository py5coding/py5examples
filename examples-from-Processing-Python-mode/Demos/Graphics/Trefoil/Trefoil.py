"""
Trefoil, Andres Colubri
A parametric surface is textured procedurally
by drawing on an offscreen PGraphics surface.
"""
from Surface import *


def setup():
    global pg, trefoil  # Py5Graphics, Py5Shape
    size(1024, 768, P3D)

    texture_mode(NORMAL)
    no_stroke()

    # Creating offscreen surface for 3D rendering.
    pg = create_graphics(32, 512, P3D)
    pg.begin_draw()
    pg.background(0, 0)
    pg.no_stroke()
    pg.fill(255, 0, 0, 200)
    pg.end_draw()

    # Saving trefoil surface into a Py5Shape3D object
    trefoil = create_trefoil(350, 60, 15, pg)


def draw():
    background(0)

    pg.begin_draw()
    pg.ellipse(random(pg.width), random(pg.height), 4, 4)
    pg.end_draw()

    ambient(250, 250, 250)
    point_light(255, 255, 255, 0, 0, 200)

    with push_matrix():
        translate(width / 2, height / 2, -200)
        rotate_x(frame_count * PI / 500)
        rotate_y(frame_count * PI / 500)
        shape(trefoil)
