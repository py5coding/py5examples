"""
Reach 3
based on code from Keith Peters.

The arm follows the position of the ball by
calculating the angles with atan2().
"""
num_segments = 8
x = [0.0] * num_segments
y = [0.0] * num_segments
angle = [0.0] * num_segments
seg_length = 26
target_x = 0
target_y = 0
ball_x = 50
ball_y = 50
ball_x_direction = 2.5
ball_y_direction = -2


def setup():
    size(640, 360)
    stroke_weight(20.0)
    stroke(255, 100)
    no_fill()
    x[-1] = width / 2  # Set base x-coordinate
    y[-1] = height  # Set base y-coordinate


def draw():
    global ball_x, ball_y
    global ball_x_direction, ball_y_direction
    background(0)
    stroke_weight(20)
    ball_x = ball_x + 1.0 * ball_x_direction
    ball_y = ball_y + 0.8 * ball_y_direction
    if ball_x > width - 25 or ball_x < 25:
        ball_x_direction *= -1
    if ball_y > height - 25 or ball_y < 25:
        ball_y_direction *= -1
    ellipse(ball_x, ball_y, 30, 30)
    reach_segment(0, ball_x, ball_y)
    for i in range(1, num_segments):
        reach_segment(i, target_x, target_y)
    for i in range(len(x) - 1, 0, -1):
        position_segment(i, i - 1)
    for i in range(len(x)):
        segment(x[i], y[i], angle[i], (i + 1) * 2)


def position_segment(a, b):
    x[b] = x[a] + cos(angle[a]) * seg_length
    y[b] = y[a] + sin(angle[a]) * seg_length


def reach_segment(i, xin, yin):
    global target_x, target_y
    dx = xin - x[i]
    dy = yin - y[i]
    angle[i] = atan2(dy, dx)
    target_x = xin - cos(angle[i]) * seg_length
    target_y = yin - sin(angle[i]) * seg_length


def segment(x, y, a, sw):
    stroke_weight(sw)
    with push_matrix():
        translate(x, y)
        rotate(a)
        line(0, 0, seg_length, 0)
