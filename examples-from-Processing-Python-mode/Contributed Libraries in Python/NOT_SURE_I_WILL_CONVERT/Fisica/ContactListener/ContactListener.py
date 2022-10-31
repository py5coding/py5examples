"""
Contacts
by Ricard Marxer
(Adapted for Python by Jonathan Feinberg.)

This example shows how to use contact events.
"""
add_library('fisica')


class ContactListener(FContactAdapter):

    """Demonstration of implementing FContactListener by subclassing
       FContactAdapter."""

    def __init__(self, obstacle):
        self.obstacle = obstacle

    def get_contacted_ball(self, c):
        if c.get_body1() == self.obstacle:
            return c.get_body2()
        if c.get_body2() == self.obstacle:
            return c.get_body1()
        return None

    def contact_started(self, c):
        ball = self.get_contacted_ball(c)
        if ball:
            ball.set_fill(30, 190, 200)

    def contact_persisted(self, c):
        ball = self.get_contacted_ball(c)
        if ball:
            ball.set_fill(30, 120, 200)
            no_stroke()
            fill(255, 220, 0)
            ellipse(c.get_x(), c.get_y(), 10, 10)

    def contact_ended(self, c):
        ball = self.get_contacted_ball(c)
        if ball:
            ball.set_fill(200, 30, 90)


def setup():
    size(400, 400)
    smooth()
    Fisica.init(this)
    global world
    world = FWorld()
    global obstacle
    obstacle = FBox(150, 150)
    obstacle.set_rotation(PI / 4)
    obstacle.set_position(width / 2, height / 2)
    obstacle.set_static(True)
    obstacle.set_fill(0)
    obstacle.set_restitution(0)
    world += obstacle
    world.set_contact_listener(ContactListener(obstacle))


def draw():
    background(255)
    if frame_count % 5 == 0:
        b = FCircle(20)
        b.set_position(width / 2 + random(-50, 50), 50)
        b.set_velocity(0, 200)
        b.set_restitution(0)
        b.set_no_stroke()
        b.set_fill(200, 30, 90)
        world += b
    world.draw()
    world.step()
    stroke_weight(1)
    stroke(255)
    for c in obstacle.get_contacts():
        line(c.get_body1().get_x(), c.get_body1().get_y(),
             c.get_body2().get_x(), c.get_body2().get_y())
