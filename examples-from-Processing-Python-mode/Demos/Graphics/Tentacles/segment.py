class Segment(object):
    '''A Segment, which encapsulates its own position and color, and can draw
    itself'''

    def __init__(self, id, tick_offset, alti, color):
        self.id = id
        #  Effectively, the distance between segments.
        self.alti = alti
        self.tick_offset = tick_offset
        self.color = color
        self.loc = Py5Vector(0.0, 0.0, 0.0)
        # A magic number. 12 just seems to look good.
        self.tick_offset *= 12

    def calc(self, time, s_radius):
        # Spherical coords.
        # New formula from http://acko.net/blog/js1k-demo-the-making-of
        lon = (cos(time + sin(time * 0.31)) * 2
               + sin(time * 0.83)
               * 3 + time * 0.02)
        lat = (sin(time * 0.7)
               - cos(3 + time * 0.23) * 3)
        # Convert to cartesian 3D.
        # http://acko.net/blog/js1k-demo-the-making-of
        self.loc.set(cos(lon) * cos(lat) * (s_radius + self.alti),
                     sin(lon) * cos(lat) * (s_radius + self.alti),
                     sin(lat) * (s_radius + self.alti))

    def draw_self(self, other):
        stroke(self.color)
        line(self.loc.x, self.loc.y, self.loc.z,
             other.loc.x, other.loc.y, other.loc.z)
