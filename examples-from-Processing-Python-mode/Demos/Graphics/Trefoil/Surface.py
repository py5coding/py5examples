"""
Code to draw a trefoil knot surface, normals and texture coordinates.
Adapted from the parametric equations example by Philip Rideout:
http://iphone-3d-programming.labs.oreilly.com/ch03.html
"""
from py5 import (
    create_shape,
    TRIANGLES,
    sin, cos, TWO_PI,
    Py5Vector
    )

def create_trefoil(s, ny, nx, tex):
    """
    This function draws a trefoil knot surface as a triangle mesh derived
    from its parametric equation.
    """

    obj = create_shape()
    obj.begin_shape(TRIANGLES)
    obj.texture(tex)

    for j in range(nx):
        u0 = j / nx
        u1 = (j + 1) / nx
        for i in range(ny):
            v0 = i / ny
            v1 = (i + 1) / ny

            p0 = eval_point(u0, v0)
            n0 = eval_normal(u0, v0)

            p1 = eval_point(u0, v1)
            n1 = eval_normal(u0, v1)

            p2 = eval_point(u1, v1)
            n2 = eval_normal(u1, v1)

            # Triangle p0-p1-p2
            obj.normal(n0.x, n0.y, n0.z)
            obj.vertex(s * p0.x, s * p0.y, s * p0.z, u0, v0)
            obj.normal(n1.x, n1.y, n1.z)
            obj.vertex(s * p1.x, s * p1.y, s * p1.z, u0, v1)
            obj.normal(n2.x, n2.y, n2.z)
            obj.vertex(s * p2.x, s * p2.y, s * p2.z, u1, v1)

            p1 = eval_point(u1, v0)
            n1 = eval_normal(u1, v0)

            # Triangle p0-p2-p1
            obj.normal(n0.x, n0.y, n0.z)
            obj.vertex(s * p0.x, s * p0.y, s * p0.z, u0, v0)
            obj.normal(n2.x, n2.y, n2.z)
            obj.vertex(s * p2.x, s * p2.y, s * p2.z, u1, v1)
            obj.normal(n1.x, n1.y, n1.z)
            obj.vertex(s * p1.x, s * p1.y, s * p1.z, u1, v0)

    obj.end_shape()
    return obj


def eval_normal(u, v):
    """
    Evaluates the surface normal corresponding to normalized parameters (u, v)
    """

    # Compute the tangents and their cross product.
    p = eval_point(u, v)
    tang_u = eval_point(u + 0.01, v)
    tang_v = eval_point(u, v + 0.01)
    tang_u -= p
    tang_v -= p

    norm_uv = tang_v.cross(tang_u)
    norm_uv.normalize()
    return norm_uv


def eval_point(u, v):
    """
    Evaluates the surface point corresponding to normalized parameters (u, v)
    """

    a, b, c, d = 0.5, 0.3, 0.5, 0.1
    s = TWO_PI * u
    t = (TWO_PI * (1 - v)) * 2

    r = a + b * cos(1.5 * t)
    x = r * cos(t)
    y = r * sin(t)
    z = c * sin(1.5 * t)

    dv = Py5Vector()
    dv.x = (-1.5 * b * sin(1.5 * t) * cos(t) -
            (a + b * cos(1.5 * t)) * sin(t))
    dv.y = (-1.5 * b * sin(1.5 * t) * sin(t) +
            (a + b * cos(1.5 * t)) * cos(t))
    dv.z = 1.5 * c * cos(1.5 * t)

    q = dv
    q.normalize()
    qvn = Py5Vector(q.y, -q.x, 0)
    qvn.normalize()
    ww = q.cross(qvn)

    pt = Py5Vector()
    pt.x = x + d * (qvn.x * cos(s) + ww.x * sin(s))
    pt.y = y + d * (qvn.y * cos(s) + ww.y * sin(s))
    pt.z = z + d * ww.z * sin(s)
    return pt
