"""
Spot.

Move the mouse the change the position and concentation
of a blue spot light.
"""

concentration = 600  # Try values 1 -> 10000


def setup():
    size(640, 360, P3D)
    no_stroke()
    fill(204)
    sphere_detail(60)


def draw():
    background(0)

    # Light the bottom of the sphere
    directional_light(51, 102, 126, 0, -1, 0)

    # Orange light on the upper-right of the sphere
    spot_light(204, 153, 0, 360, 160, 600, 0, 0, -1, PI / 2, 600)

    # Moving spotlight that follows the mouse
    spot_light(102, 153, 204, 360, mouse_y, 600, 0, 0, -1, PI / 2, 600)

    translate(width / 2, height / 2, 0)
    sphere(120)
