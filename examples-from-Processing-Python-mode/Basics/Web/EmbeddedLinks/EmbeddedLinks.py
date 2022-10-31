"""
Loading URLs.

Click on the button to open a URL in a browser
"""
import webbrowser

over_button = False

def setup():
    size(640, 360)

def draw():
    background(204)
    if over_button:
        fill(255)
    else:
        no_fill()
    rect(105, 60, 75, 75)
    line(135, 105, 155, 85)
    line(140, 85, 155, 85)
    line(155, 85, 155, 100)

def mouse_pressed():
    if over_button:
        webbrowser.open("http://www.processing.org", 1, False)

def mouse_moved():
    check_buttons()

def mouse_dragged():
    check_buttons()

def check_buttons():
    global over_button
    over_button = 105 < mouse_x < 180 and 60 < mouse_y < 135
