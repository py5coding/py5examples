from py5 import *

class Cube(object):

    def __init__(self, w, h, d, shift_x, shift_y, shift_z):
        self.w = w
        self.h = h
        self.d = d
        self.shift_x = shift_x
        self.shift_y = shift_y
        self.shift_z = shift_z
        self.minus_w_two = -self.w / 2
        self.minus_h_two = -self.h / 2
        self.minus_d_two = -self.d / 2

    # Main cube drawing method, which looks more confusing than it really is.
    # It's just a bunch of rectangles drawn for each cube face.
    def draw_cube(self):
        with begin_shape(QUADS):
            # Front face.
            vertex(self.minus_w_two + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.minus_d_two + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.minus_d_two + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.h + self.shift_y,
                   self.minus_d_two + self.shift_z)
            vertex(self.minus_w_two + self.shift_x,
                   self.h + self.shift_y,
                   self.minus_d_two + self.shift_z)

            # Back face.
            vertex(self.minus_w_two + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.d + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.d + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.h + self.shift_y,
                   self.d + self.shift_z)
            vertex(self.minus_w_two + self.shift_x,
                   self.h + self.shift_y,
                   self.d + self.shift_z)

            # Left face.
            vertex(self.minus_w_two + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.minus_d_two + self.shift_z)
            vertex(self.minus_w_two + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.d + self.shift_z)
            vertex(self.minus_w_two + self.shift_x,
                   self.h + self.shift_y,
                   self.d + self.shift_z)
            vertex(self.minus_w_two + self.shift_x,
                   self.h + self.shift_y,
                   self.minus_d_two + self.shift_z)

            # Right face.
            vertex(self.w + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.minus_d_two + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.d + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.h + self.shift_y,
                   self.d + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.h + self.shift_y,
                   self.minus_d_two + self.shift_z)

            # Top face.
            vertex(self.minus_w_two + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.minus_d_two + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.minus_d_two + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.d + self.shift_z)
            vertex(self.minus_w_two + self.shift_x,
                   self.minus_h_two + self.shift_y,
                   self.d + self.shift_z)

            # Bottom face.
            vertex(self.minus_w_two + self.shift_x,
                   self.h + self.shift_y,
                   self.minus_d_two + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.h + self.shift_y,
                   self.minus_d_two + self.shift_z)
            vertex(self.w + self.shift_x,
                   self.h + self.shift_y,
                   self.d + self.shift_z)
            vertex(self.minus_w_two + self.shift_x,
                   self.h + self.shift_y,
                   self.d + self.shift_z)

        # Add some rotation to each box for pizazz.
        rotate_y(radians(1))
        rotate_x(radians(1))
        rotate_z(radians(1))
