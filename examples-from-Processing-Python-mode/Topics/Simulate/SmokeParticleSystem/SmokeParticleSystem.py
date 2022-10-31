"""
Smoke Particle System
by Daniel Shiffman.

A basic smoke effect using a particle system. Each particle
is rendered as an alpha masked image.
"""

from particle import Particle
from particle_system import ParticleSystem

ps = None


def setup():
    global ps
    size(640, 360)
    img = load_image("texture.png")
    ps = ParticleSystem(0, Py5Vector(width / 2, height - 60), img)


def draw():
    background(0)
    # Calculate a "wind" force based on mouse horizontal position.
    dx = map(mouse_x, 0, width, -0.2, 0.2)
    wind = Py5Vector(dx, 0)
    ps.apply_force(wind)
    ps.run()
    for i in range(2):
        ps.add_particle()
    # Draw an arrow representing the wind force.
    draw_vector(wind, Py5Vector(width / 2, 50, 0), 500)


# Renders a vector object 'v' as an arrow and a location 'loc'.
def draw_vector(v, loc, scayl):
    with push_matrix():
        arrowsize = 4
        # Translate to location to render vector.
        translate(loc.x, loc.y)
        stroke(255)
        # Call vector heading function to get direction (note that pointing up is
        # a heading of 0) and rotate.
        rotate(v.heading)
        # Calculate length of vector & scale it to be bigger or smaller if
        # necessary.
        len = v.mag * scayl
        # Draw three lines to make an arrow (draw pointing up since we've rotate
        # to the proper direction).
        line(0, 0, len, 0)
        line(len, 0, len - arrowsize, +arrowsize / 2)
        line(len, 0, len - arrowsize, -arrowsize / 2)
