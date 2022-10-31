"""
There are a number of functions that must eventually be followed by a
partner function that 'pops' or 'closes' some context created by the
first function. For example, every push_matrix() must eventually be
followed by a pop_matrix().

Python mode provides all of the same functions, but also takes advantage
of the Python language's 'with' statement to provide automatic context
management.

So, for example, instead of

    push_matrix()
    translate(10, 10)
    rotate(PI/3)
    rect(0, 0, 10, 10)
    pop_matrix()
    rect(0, 0, 10, 10)

you can write

    with push_matrix():
        translate(10, 10)
        rotate(PI/3)
        rect(0, 0, 10, 10)
    rect(0, 0, 10, 10)

This has two advantages: indentation clearly reveals which lines of
code are executed while the matrix is pushed, and you can't forget
to pop_matrix(). Also, there's less code, which means fewer bugs!

You can also use 'with' statements in these contexts:

Use this:                        Instead of this:

with push_style():                push_style()
    do_something()                do_something()
                                 pop_style()


with begin_contour():             begin_contour()
    do_something()                do_something()
                                 end_contour()


with begin_camera():              begin_camera()
    do_something()                do_something()
                                 end_camera()

with begin_pgl():                 begin_pgl()
    do_something()                do_something()
                                 end_pgl()

with begin_shape():               begin_shape()
    vertex(x, y)                 vertex(x, y)
    vertex(j, k)                 vertex(j,k)
                                 end_shape()


with begin_shape(TRIANGLES):      begin_shape(TRIANGLES)
    vertex(x, y)                 vertex(x, y)
    vertex(j, k)                 vertex(x, y)
                                 end_shape()

with begin_closed_shape():         begin_shape()
    vertex(x, y)                 vertex(x, y)
    vertex(j, k)                 vertex(j, k)
                                 end_shape(CLOSED)
"""
size(250, 180)
background(0)

fill('#FF0000')
# This should be red and at absolute 10, 10
ellipse(10, 10, 10, 10)
fill('#0000FF')
with push_style():
    fill('#00FF00')
    with push_matrix():
        translate(10, 10)
        # This should be green and at absolute 20, 20:
        ellipse(10, 10, 10, 10)
# This should be blue and at absolute 30, 30:
ellipse(30, 30, 10, 10)

fill(255)
stroke(180)

with push_matrix():
    translate(50, 0)
    with begin_closed_shape():
        vertex(0, 20)
        vertex(20, 20)
        vertex(20, 40)
        vertex(40, 40)
        vertex(40, 60)
        vertex(0, 60)

    translate(50, 0)
    with begin_shape(QUAD_STRIP):
        vertex(0, 20)
        vertex(0, 75)
        vertex(20, 20)
        vertex(20, 75)
        vertex(35, 20)
        vertex(35, 75)
        vertex(55, 20)
        vertex(55, 75)

    translate(70, 0)
    with begin_shape(LINES):
        vertex(0, 20)
        vertex(55, 20)
        vertex(55, 75)
        vertex(0, 75)

with push_matrix():
    translate(10, 80)
    with begin_shape(TRIANGLE_STRIP):
        vertex(0, 75)
        vertex(10, 20)
        vertex(20, 75)
        vertex(30, 20)
        vertex(40, 75)
        vertex(50, 20)
        vertex(60, 75)

    translate(70, 0)
    with begin_shape(TRIANGLE_FAN):
        vertex(35.5, 50)
        vertex(35.5, 15)
        vertex(70, 50)
        vertex(35.5, 85)
        vertex(0, 50)
        vertex(35.5, 15)

    translate(90, 0)
    with begin_shape(QUADS):
        vertex(0, 20)
        vertex(0, 75)
        vertex(20, 75)
        vertex(20, 20)
        vertex(35, 20)
        vertex(35, 75)
        vertex(55, 75)
        vertex(55, 20)
