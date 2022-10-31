from shape3d import Shape3D


class Icosahedron(Shape3D):

    def __init__(self, radius=150):
        Shape3D.__init__(self)
        self.top_pent = [Py5Vector() for _ in range(5)]
        self.bottom_pent = [Py5Vector() for _ in range(5)]
        c = dist(cos(0) * radius,
                 sin(0) * radius,
                 cos(radians(72)) * radius,
                 sin(radians(72)) * radius)
        b = radius
        a = sqrt((c**2) - (b**2))
        self.tri_height = sqrt((c**2) - (c / 2)**2)
        angle = 0
        for i in range(5):
            self.top_pent[i] = Py5Vector(cos(angle) * radius,
                                         sin(angle) * radius,
                                         self.tri_height / 2.0)
            angle += radians(72)
        self.top_point = Py5Vector(0, 0, self.tri_height / 2.0 + a)
        angle = 72.0 / 2.0
        for i in range(5):
            self.bottom_pent[i] = Py5Vector(cos(angle) * radius,
                                            sin(angle) * radius,
                                            -self.tri_height / 2.0)
            angle += radians(72)
        self.bottom_point = Py5Vector(0, 0, -(self.tri_height / 2.0 + a))

    # Draw icosahedron.
    def create(self):
        for i in range(5):
            if i < 4:
                # Icosahedron top.
                self.make_triangle(self.top_pent[i],
                                   self.top_point,
                                   self.top_pent[i + 1])
                # Icosahedron bottom.
                self.make_triangle(self.bottom_pent[i],
                                   self.bottom_point,
                                   self.bottom_pent[i + 1])
            else:
                self.make_triangle(self.top_pent[i],
                                   self.top_point,
                                   self.top_pent[0])
                self.make_triangle(self.bottom_pent[i],
                                   self.bottom_point,
                                   self.bottom_pent[0])

        # Icosahedron body.
        for i in range(5):
            if i < 3:
                self.make_triangle(self.top_pent[i],
                                   self.bottom_pent[i + 1],
                                   self.bottom_pent[i + 2])
                self.make_triangle(self.bottom_pent[i + 2],
                                   self.top_pent[i],
                                   self.top_pent[i + 1])
            elif i == 3:
                self.make_triangle(self.top_pent[i],
                                   self.bottom_pent[i + 1],
                                   self.bottom_pent[0])
                self.make_triangle(self.bottom_pent[0],
                                   self.top_pent[i],
                                   self.top_pent[i + 1])
            elif i == 4:
                self.make_triangle(self.top_pent[i],
                                   self.bottom_pent[0],
                                   self.bottom_pent[1])
                self.make_triangle(self.bottom_pent[1],
                                   self.top_pent[i],
                                   self.top_pent[0])

    def make_triangle(self, a, b, c):
        with begin_shape():
            vertex(a.x, a.y, a.z)
            vertex(b.x, b.y, b.z)
            vertex(c.x, c.y, c.z)
