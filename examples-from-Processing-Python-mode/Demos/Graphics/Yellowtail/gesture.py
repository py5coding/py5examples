from py5 import sqrt, mag
from java.awt import Polygon
from vec3f import Vec3f

capacity = 300  # Originally 600 
damp = 5.0
damp_inv = 1.0 / damp
damp1 = damp - 1
INIT_TH = 14


class Gesture(object):
    __slots__= (
        'w', 'h', 'path', 'polygons', 'crosses',
        'n_polys', 'jump_dx', 'jump_dy',
        'n_points', 'exists', 'thickness',
        )
    
    def __init__(self, mw, mh):
        self.w = mw
        self.h = mh
        self.path = [Vec3f() for _ in range(capacity)]
        self.polygons = [Polygon() for _ in range(capacity)]
        for p in self.polygons:
            p.npoints = 4
        self.crosses = [0, ] * capacity
        self.n_polys = 0
        self.jump_dx = 0
        self.jump_dy = 0

        self.clear()

    def clear(self):
        self.n_points = 0
        self.exists = False
        self.thickness = INIT_TH

    def clear_polys(self):
        self.n_polys = 0

    def add_point(self, x, y):
        if self.n_points >= capacity:
            # there are all sorts of possible solutions here,
            # but for abject simplicity, I don't do anything.
            pass
        else:
            v = self.dist_to_last(x, y)
            p = self.get_pressure_from_velocity(v)
            self.path[self.n_points].set(x, y, p)
            self.n_points += 1
            if self.n_points > 1:
                self.exists = True
                self.jump_dx = self.path[self.n_points - 1].x - self.path[0].x
                self.jump_dy = self.path[self.n_points - 1].y - self.path[0].y

    def get_pressure_from_velocity(self, v):
        scale_ = 18
        min_p = 0.02
        if self.n_points > 0:
            old_p = self.path[self.n_points - 1].p
        else:
            old_p = 0
        return ((min_p + max(0, 1.0 - v / scale_)) + (damp1 * old_p)) * damp_inv

    def set_pressures():
        # pressures vary from 0...1
        t = 0
        u = 1.0 / (self.n_points - 1) * TWO_PI
        for i in range(self.n_points):
            self.path[i].p = sqrt((1.0 - cos(t)) * 0.5)
            t += u

    def dist_to_last(self, ix, iy):
        if self.n_points > 0:
            v = self.path[self.n_points - 1]
            dx = v.x - ix
            dy = v.y - iy
            return mag(dx, dy)
        else:
            return 30

    def compile(self):
        # compute the polygons from the path of Vec3f's
        if not self.exists:
            return
        self.clear_polys()
        taper = 1.0
        n_path_points = self.n_points - 1
        last_poly_index = n_path_points - 1
        npm1finv = 1.0 / max(1, n_path_points - 1)
        # handle the first point
        p0 = self.path[0]
        p1 = self.path[1]
        radius0 = p0.p * self.thickness
        dx01 = p1.x - p0.x
        dy01 = p1.y - p0.y
        hp01 = sqrt(dx01 * dx01 + dy01 * dy01)
        if hp01 == 0:
            hp01 = 0.0001

        co01 = radius0 * dx01 / hp01
        si01 = radius0 * dy01 / hp01
        ax = p0.x - si01
        ay = p0.y + co01
        bx = p0.x + si01
        by = p0.y - co01
        xpts = []
        ypts = []
        LC = 20
        RC = self.w - LC
        TC = 20
        BC = self.h - TC
        mint = 0.618
        tapow = 0.4
        # handle the middle points
        i = 1
        for i in range(1, n_path_points):
            taper = pow((last_poly_index - i) * npm1finv, tapow)
            p0 = self.path[i - 1]
            p1 = self.path[i]
            p2 = self.path[i + 1]
            p1x = p1.x
            p1y = p1.y
            radius1 = max(mint, taper * p1.p * self.thickness)
            # assumes all segments are roughly the same length...
            dx02 = p2.x - p0.x
            dy02 = p2.y - p0.y
            hp02 = sqrt(dx02 * dx02 + dy02 * dy02)
            if hp02 != 0:
                hp02 = radius1 / hp02

            co02 = dx02 * hp02
            si02 = dy02 * hp02
            # translate the integer coordinates to the viewing rectangle
            axi = axip = ax
            ayi = ayip = ay
            axi = self.w - (-axi % self.w) if axi < 0 else axi % self.w
            axid = axi - axip
            ayi = self.h - (-ayi % self.h) if ayi < 0 else ayi % self.h
            ayid = ayi - ayip
            # set the vertices of the polygon
            apoly = self.polygons[self.n_polys]
            self.n_polys += 1
            xpts = apoly.xpoints
            ypts = apoly.ypoints
            axi = int(axid + axip)
            xpts[0] = axi
            bxi = int(axid + bx)
            xpts[1] = bxi
            cx = p1x + si02
            cxi = int(axid + cx)
            xpts[2] = cxi
            dx = p1x - si02
            dxi = int(axid + dx)
            xpts[3] = dxi
            ayi = int(ayid + ayip)
            ypts[0] = ayi
            byi = int(ayid + by)
            ypts[1] = byi
            cy = p1y - co02
            cyi = int(ayid + cy)
            ypts[2] = cyi
            dy = p1y + co02
            dyi = int(ayid + dy)
            ypts[3] = dyi
            # keep a record of where we cross the edge of the screen
            self.crosses[i] = 0
            if (axi <= LC) or (bxi <= LC) or (cxi <= LC) or (dxi <= LC):
                self.crosses[i] |= 1

            if (axi >= RC) or (bxi >= RC) or (cxi >= RC) or (dxi >= RC):
                self.crosses[i] |= 2

            if (ayi <= TC) or (byi <= TC) or (cyi <= TC) or (dyi <= TC):
                self.crosses[i] |= 4

            if (ayi >= BC) or (byi >= BC) or (cyi >= BC) or (dyi >= BC):
                self.crosses[i] |= 8

            # swap data for next time
            ax = dx
            ay = dy
            bx = cx
            by = cy

        # handle the last point
        p2 = self.path[n_path_points]
        apoly = self.polygons[self.n_polys]
        self.n_polys += 1
        xpts = apoly.xpoints
        ypts = apoly.ypoints
        xpts[0] = int(ax)
        xpts[1] = int(bx)
        xpts[2] = int(p2.x)
        xpts[3] = int(p2.x)
        ypts[0] = int(ay)
        ypts[1] = int(by)
        ypts[2] = int(p2.y)
        ypts[3] = int(p2.y)

    def smooth(self):
        # average neighboring points
        weight = 18
        scale = 1.0 / (weight + 2)
        for i in range(1, self.n_points - 2):
            lower = self.path[i - 1]
            center = self.path[i]
            upper = self.path[i + 1]
            center.x = (lower.x + weight * center.x + upper.x) * scale
            center.y = (lower.y + weight * center.y + upper.y) * scale
