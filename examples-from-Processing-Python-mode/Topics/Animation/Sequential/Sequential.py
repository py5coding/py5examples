"""
Sequential
by James Paterson.

Displaying a sequence of images creates the illusion of motion.
Twelve images are loaded and each is displayed individually in a loop.
"""

num_frames = 12  # The number of frames in the animation
images = [Py5Image] * num_frames


def setup():
    size(640, 360)
    frame_rate(24)

    images[0] = load_image("PT_anim0000.gif")
    images[1] = load_image("PT_anim0001.gif")
    images[2] = load_image("PT_anim0002.gif")
    images[3] = load_image("PT_anim0003.gif")
    images[4] = load_image("PT_anim0004.gif")
    images[5] = load_image("PT_anim0005.gif")
    images[6] = load_image("PT_anim0006.gif")
    images[7] = load_image("PT_anim0007.gif")
    images[8] = load_image("PT_anim0008.gif")
    images[9] = load_image("PT_anim0009.gif")
    images[10] = load_image("PT_anim0010.gif")
    images[11] = load_image("PT_anim0011.gif")

    # If you don't want to load each image separately
    # and you know how many frames you have, you
    # can create the filenames as the program runs.
    # The nf() command does number formatting, which will
    # ensure that the number is (in this case) 4 digits.
    # Using a list comprehension:
    # images = [loadImage('PT_anim' + nf(i, 4) + '.gif')
    #           for i in range(numFrames)]
    #


def draw():
    background(0)
    # Use % to cycle through frames
    current_frame = (frame_count + 1) % num_frames
    offset = 0
    for x in range(-100, width, images[0].width):
        image(images[(current_frame + offset) % num_frames], x, -20)
        offset += 2
        image(images[(current_frame + offset) % num_frames], x, height / 2)
        offset += 2
