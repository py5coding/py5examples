"""
Ignore Styles.
Illustration by George Brower.

Shapes are loaded with style information that tells them how
to draw (the color, stroke weight, etc.) The disable_style()
method of Py5Shape turns off this information. The enable_style()
method turns it back on.
"""


def setup():
    size(640, 360)
    # The file "bot1.svg" must be in the data folder
    # of the current sketch to load successfully
    global bot
    bot = load_shape("bot1.svg")
    no_loop()


def draw():
    background(102)

    # Draw left bot
    bot.disable_style()    # Ignore the colors in the SVG
    fill(0, 102, 153)     # Set the SVG fill to blue
    stroke(255)           # Set the SVG fill to white
    shape(bot, 20, 25, 300, 300)
    # Draw right bot
    bot.enable_style()
    shape(bot, 320, 25, 300, 300)
