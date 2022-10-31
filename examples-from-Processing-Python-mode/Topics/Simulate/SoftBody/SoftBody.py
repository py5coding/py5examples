"""
Soft Body
by Ira Greenberg.

Softbody dynamics simulation using curve_vertex() and curve_tightness().
"""

# center point
center_x = 0
center_y = 0
radius = 45
rot_angle = -90
accel_x = 0
accel_y = 0
springing = .0009
damping = .98
# Corner nodes
nodes = 5
node_start_x = [0.0] * nodes
node_start_y = [0.0] * nodes
node_x = [0.0] * nodes
node_y = [0.0] * nodes
angle = [0.0] * nodes
frequency = [0.0] * nodes
# Soft-body dynamics
organic_constant = 1


def setup():
    size(640, 360)
    # Center shape in window.
    center_x = width / 2
    center_y = height / 2
    # Initialize frequencies for corner nodes.
    for i in range(nodes):
        frequency[i] = random(5, 12)
    no_stroke()
    frame_rate(30)


def draw():
    # fade background
    fill(0, 100)
    rect(0, 0, width, height)
    draw_shape()
    move_shape()


def draw_shape():
    global rot_angle
    # Calculate node starting locations.
    for i in range(nodes):
        node_start_x[i] = center_x + cos(radians(rot_angle)) * radius
        node_start_y[i] = center_y + sin(radians(rot_angle)) * radius
        rot_angle += 360.0 / nodes
    # Draw polygon.
    curve_tightness(organic_constant)
    fill(255)
    with begin_closed_shape():
        for i in range(nodes):
            curve_vertex(node_x[i], node_y[i])
        for i in range(nodes - 1):
            curve_vertex(node_x[i], node_y[i])


def move_shape():
    global center_x, center_y, delta_x, delta_y, accel_x, accel_y
    # Move center point.
    delta_x = mouse_x - center_x
    delta_y = mouse_y - center_y
    # Create springing effect.
    delta_x *= springing
    delta_y *= springing
    accel_x += delta_x
    accel_y += delta_y
    # Move predator's center.
    center_x += accel_x
    center_y += accel_y
    # Slow down springing.
    accel_x *= damping
    accel_y *= damping
    # Change curve tightness.
    organic_constant = 1 - ((abs(accel_x) + abs(accel_y)) * .1)
    # Move nodes.
    for i in range(nodes):
        node_x[i] = node_start_x[i] + sin(radians(angle[i])) * (accel_x * 2)
        node_y[i] = node_start_y[i] + sin(radians(angle[i])) * (accel_y * 2)
        angle[i] += frequency[i]
