"""
Circle Collision with Swapping Velocities.
by Ira Greenberg.

Based on Keith Peter's Solution in
"Foundation Actionscript Animation: Making Things Move!".
"""
from ball import Ball

balls = [Ball(100, 400, 20), Ball(700, 400, 80)]


def setup():
    size(640, 360)


def draw():
    background(51)
    for ball in balls:
        ball.update()
        ball.display()
        ball.check_boundary_collision()
    balls[0].check_collision(balls[1])
