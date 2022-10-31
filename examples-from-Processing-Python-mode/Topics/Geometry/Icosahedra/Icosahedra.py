"""
I Like Icosahedra
by Ira Greenberg.

This example plots icosahedra. The Icosahdron is a regular polyhedron composed
of twenty equalateral triangles.
Slightly simplified to reduce the complexity of the Shape3D class and remove
the unused Dimension3D class.
"""
from icosahedron import Icosahedron

# Pre-calculate some global values
ico1_x_rot = PI / 185
ico1_y_rot = PI / -200
ico2_x_rot = PI / 200
ico2_y_rot = PI / 300
ico_x3_rot = PI / -200
ico_y3_rot = PI / 200


def setup():
    global half_width, half_height, ico3_x_offset, ico1_x_offset, ico1, ico2, ico3
    size(640, 360, P3D)
    half_width = width / 2
    half_height = height / 2
    ico3_x_offset = width / 3.5
    ico1_x_offset = ico3_x_offset * -1
    ico1 = Icosahedron(75)
    ico2 = Icosahedron(75)
    ico3 = Icosahedron(75)


def draw():
    background(0)
    lights()
    translate(half_width, half_height)

    with push_matrix():
        translate(ico1_x_offset, 0)
        rotate_x(frame_count * ico1_x_rot)
        rotate_y(frame_count * ico1_y_rot)
        stroke(170, 0, 0)
        no_fill()
        ico1.create()

    with push_matrix():
        rotate_x(frame_count * ico2_x_rot)
        rotate_y(frame_count * ico2_y_rot)
        stroke(150, 0, 180)
        fill(170, 170, 0)
        ico2.create()

    with push_matrix():
        translate(ico3_x_offset, 0)
        rotate_x(frame_count * ico_x3_rot)
        rotate_y(frame_count * ico_y3_rot)
        no_stroke()
        fill(0, 0, 185)
        ico3.create()
