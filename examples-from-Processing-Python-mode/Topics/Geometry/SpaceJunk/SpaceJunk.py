"""
Space Junk
by Ira Greenberg (zoom suggestion by Danny Greenberg).

Rotating cubes in space using a custom Cube class. Color controlled by light
sources. Move the mouse left and right to zoom.
"""
from cube import Cube

# Used for overall rotation.
angle = 0
# Cube count - lower / raise to test performance.
limit = 500
# Instantiate cubes, passing in random vals for size and postion.
cubes = [Cube(random(-10, 10), random(-10, 10), random(-10, 10),
              random(-140, 140), random(-140, 140), random(-140, 140))
         for _ in range(limit)]

def setup():
    global half_width, half_height
    size(640, 360, P3D)
    background(0)
    no_stroke()
    half_width = width / 2
    half_height = height / 2

def draw():
    global angle
    background(0)
    fill(200)
    # Set up some different colored lights
    point_light(51, 102, 255, 65, 60, 100)
    point_light(200, 40, 60, -65, -60, -150)
    # Raise overall light in scene
    ambient_light(70, 70, 10)
    # Center geometry in display window. Change the 3rd argument ('0.65')
    # to move the block group nearer(+) or farther(-)
    translate(half_width, half_height, -200 + mouse_x * 0.65)
    # Rotate around y and x axes
    rotate_y(radians(angle))
    rotate_x(radians(angle))
    # Draw cubes
    for cube in cubes:
        cube.draw_cube()
    # Used in rotate function calls above
    angle += 0.2
