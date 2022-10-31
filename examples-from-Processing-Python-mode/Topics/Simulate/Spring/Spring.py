"""
Spring.

Click, drag, and release the horizontal bar to start the spring.
"""

# Spring drawing constants for top bar
spring_height = 32  # Height
left = 0      # Left position
right = 0     # Right position
max_height = 200     # Maximum Y value
min_height = 100     # Minimum Y value
over = False  # If mouse over
move = False  # If mouse down and over
# Spring simulation constants
M = 0.8   # Mass
K = 0.2   # Spring constant
D = 0.92  # Damping
R = 150   # Rest position
# Spring simulation variables
ps = R    # Position
v = 0.0   # Velocity
a = 0     # Acceleration
f = 0     # Force


def setup():
    global left, right
    size(640, 360)
    rect_mode(CORNERS)
    no_stroke()
    left = width / 2 - 100
    right = width / 2 + 100


def draw():
    background(102)
    update_spring()
    draw_spring()


def draw_spring():
    # Draw base
    fill(0.2)
    base_width = 0.5 * ps + -8
    rect(width / 2 - base_width, ps + spring_height,
         width / 2 + base_width, height)
    # Set color and draw top bar.
    if over or move:
        fill(255)
    else:
        fill(204)
    rect(left, ps, right, ps + spring_height)


def update_spring():
    global over, f, ps, a, v
    # Update the spring position.
    if not move:
        f = -K * (ps - R)  # f=-ky
        a = f / M  # Set the acceleration. f=ma == a=f/m
        v = D * (v + a)  # Set the velocity.
        ps = ps + v  # Updated position
    if abs(v) < 0.1:
        v = 0.0
    # Test if mouse is over the top bar
    over = (left < mouse_x < right) and (ps < mouse_y < ps + spring_height)
    # Set and constrain the position of top bar.
    if move:
        ps = mouse_y - spring_height / 2
        if ps > max_height:
            ps = max_height
        elif ps < min_height:
            ps = min_height


def mouse_pressed():
    global move
    if over:
        move = True


def mouse_released():
    global move
    move = False
