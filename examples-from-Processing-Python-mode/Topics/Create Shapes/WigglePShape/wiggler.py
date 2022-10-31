# An object that wraps the PShape.
class Wiggler(object):

    def __init__(self):
        # For 2D Perlin noise
        self.yoff = 0
        # Its location
        self.x = width / 2
        self.y = height / 2
        # The "original" locations of the vertices make up a circle.
        # We are using a list to keep a duplicate copy
        # of vertices original locations.
        self.original = []
        for a in range(0, int(TWO_PI * 10), 2):
            ascaled = a * .1
            v = Py5Vector.from_heading(ascaled)
            v *= 100
            self.original.append(v)
        # The PShape to be "wiggled".
        # Make the PShape with those vertices.
        self.s = create_shape()
        self.s.begin_shape()
        self.s.fill(127)
        self.s.stroke(0)
        self.s.stroke_weight(2)
        for v in self.original:
            self.s.vertex(v.x, v.y)
        self.s.end_shape(CLOSE)

    def wiggle(self):
        xoff = 0
        # Apply an offset to each vertex.
        for i in range(self.s.get_vertex_count()):
            # Calculate a vertex location based on noise around "original"
            # location.
            pos = self.original[i]
            a = TWO_PI * noise(xoff, self.yoff)
            r = Py5Vector.from_heading(a)
            r *= 4
            r += pos
            # Set the location of each vertex to the one.
            self.s.set_vertex(i, r.x, r.y)
            # Increment perlin noise x value.
            xoff += 0.5
        # Increment perlin noise y value.
        self.yoff += 0.02

    def display(self):
        with push_matrix():
            translate(self.x, self.y)
            shape(self.s)
