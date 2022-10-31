from segment import Segment


class Tentacle(object):
    '''A Tentacle made of Segments.
    '''
    # Factor to determine the distance between Segments.
    AltiOffset = 1

    def __init__(self, time_offset, palette):
        self.time_offset = time_offset
        self.palette = palette
        self.segments = [Segment(i, i,  # Second `i` is tickOffset.
                                 (Tentacle.AltiOffset * i) + i,
                                 self.palette[i])
                         for i in range(5)]

    def update(self, time, Tick, s_radius):
        for seg in self.segments:
            seg.calc((time - self.time_offset) - (seg.tick_offset * Tick),
                     s_radius)
            # Don't try to draw *from* the last segment.
            if seg.id != len(self.segments) - 1:
                # Draw from this segment to the next segment.
                seg.draw_self(self.segments[seg.id + 1])
