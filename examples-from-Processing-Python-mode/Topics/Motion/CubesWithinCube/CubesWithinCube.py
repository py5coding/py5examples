"""
Cubes Contained Within a Cube
by Ira Greenberg.

Collision detection against all outer cube's surfaces.
"""
from cube import Cube


Bounds = 300
# 20 little internal cubes
cubes = []
for _ in range(20):
    # Cubes are randomly sized
    cube_size = random(5, 15)
    cubes.append(Cube(cube_size, cube_size, cube_size))


def setup():
    size(640, 360, P3D)
    global half_width, half_height
    half_width = width / 2.0
    half_height = height / 2.0


def draw():
    background(50)
    lights()

    # Center in display window
    translate(half_width, half_height, -130)

    # Rotate everything, including external large cube
    rotate_x(frame_count * 0.001)
    rotate_y(frame_count * 0.002)
    rotate_z(frame_count * 0.001)
    stroke(255)

    # Outer transparent cube, just using box() method
    no_fill()
    box(Bounds)

    # Move and rotate cubes
    for cube in cubes:
        cube.update(Bounds)
        cube.display()
