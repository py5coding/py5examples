"""
Pie Chart

Uses the arc() function to generate a pie chart from the data
stored in a tuple.
"""
angles = (30, 10, 45, 35, 60, 38, 75, 67)


def setup():
    size(640, 360)
    no_stroke()
    no_loop()    # Run once and stop


def draw():
    background(100)
    pie_chart(300, angles)


def pie_chart(diameter, data):
    last_angle = 0
    for i, angle in enumerate(data):
        gray = map(i, 0, len(data), 0, 255)
        fill(gray)
        arc(width / 2, height / 2, diameter, diameter,
            last_angle, last_angle + radians(angle))
        last_angle += radians(angle)
