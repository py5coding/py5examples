"""
Keyboard Functions.
Modified from code by Martin.
Original 'Color Typewriter' concept by John Maeda.

Click on the window to give it focus and press the letter keys to type colors.
The keyboard function key_pressed() is called whenever
a key is pressed. key_released() is another keyboard
function that is called when a key is released.
"""

A_code = ord('A')
Z_code = ord('Z')
a_code = ord('a')
z_code = ord('z')

max_height = 40
min_height = 20
letter_height = max_height  # Height of the letters
letter_width = 20  # Width of the letter

x = -letter_width  # X position of the letters
y = 0  # Y position of the letters

newletter = False

num_chars = 26  # There are 26 characters in the alphabet
colors = []


def setup():
    size(640, 360)
    no_stroke()
    color_mode(HSB, num_chars)
    background(num_chars / 2)
    # Set a gray value for each key
    for i in range(0, num_chars, 1):
        colors.append(color(i, num_chars, num_chars))


def draw():
    global newletter
    if newletter:
        # Draw the letter
        if letter_height == max_height:
            y_pos = y
            rect(x, y_pos, letter_width, letter_height)
        else:
            y_pos = y + min_height
            rect(x, y_pos, letter_width, letter_height)
            fill(num_chars / 2)
            rect(x, y_pos - min_height, letter_width, letter_height)
        newletter = False


def key_pressed():
    global newletter, x, y, letter_height
    if key != CODED:
        key_code = ord(key)
    else:
        key_code = key_code
    # If the key is between 'A'(65) to 'Z' and 'a' to 'z'(122)
    if A_code <= key_code <= Z_code or a_code <= key_code <= z_code:
        if key_code <= Z_code:
            key_index = key_code - A_code
            letter_height = max_height
            fill(colors[key_code - A_code])
        else:
            key_index = key_code - a_code
            letter_height = min_height
            fill(colors[key_code - a_code])
    else:
        fill(0)
        letter_height = 10

    newletter = True

    # Update the "letter" position
    x = (x + letter_width)

    # Wrap horizontally
    if x > width - letter_width:
        x = 0
        y += max_height

    # Wrap vertically
    if y > height - letter_height:
        y = 0  # reset y to 0
