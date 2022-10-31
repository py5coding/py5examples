"""
Primitives 3_d.

Placing mathematically 3D objects in synthetic space.
The lights() method reveals their imagined dimension.
The box() and sphere() functions each have one parameter
which is used to specify their size. These shapes are
positioned using the translate() function.
"""

size(640, 360, P3D)
background(0)
lights()
no_stroke()
with push_matrix():
    translate(130, height / 2, 0)
    rotate_y(1.25)
    rotate_x(-0.4)
    box(100)
no_fill()
stroke(255)
with push_matrix():
    translate(500, height * 0.35, -200)
    sphere(280)
