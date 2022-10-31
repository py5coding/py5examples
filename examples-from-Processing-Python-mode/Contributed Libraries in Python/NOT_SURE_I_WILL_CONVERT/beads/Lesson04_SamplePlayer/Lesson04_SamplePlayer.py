add_library('beads')

ac = AudioContext()


def setup():
    size(600, 100)
    select_input("Select an audio file:", "fileSelected")


def file_selected(selection):
    """
    Here's how to play back a sample.

    The first line gives you a way to choose the audio file.
    The (commented, optional) second line allows you to stream the audio rather than loading it all at once.
    The third line creates a sample player and loads in the Sample.
    SampleManager is a utility which keeps track of loaded audio
    files according to their file names, so you don't have to load them again.
    """
    if not selection:
        exit()
    audio_file_name = selection.get_absolute_path()
    sample = SampleManager.sample(audio_file_name)
    player = SamplePlayer(ac, sample)
    # And as before...
    g = Gain(ac, 2, 0.4)
    g.add_input(player)
    ac.out.add_input(g)
    ac.start()
    """
    Note there is a lot more you can do. e.g., Varispeed. Try adding...
        speed_control = Envelope(ac, 1)
        player.set_rate(speed_control)
        speed_control.add_segment(1, 1000)    # wait a second
        speed_control.add_segment(-0.5, 3000) # now rewind
    """

# Here's the code to draw a waveform.
# The code draws the current buffer of audio across the
# width of the window. To find out what a buffer of audio
# is, read on.


# Start with some spunky colors.
fore = color(255, 102, 204)
back = color(0, 0, 0)


def draw():
    no_stroke()
    background(back)
    # scan across the pixels
    for i in range(width):
        # for each pixel work out where in the current audio buffer we are
        buff_index = i * ac.get_buffer_size() / width
        # then work out the pixel height of the audio data at that point
        v_offset = int((1 + 5 * ac.out.get_value(0, buff_index)) * height / 2)
        v_offset = min(v_offset, height)
        fill(fore)
        ellipse(i, v_offset, 3, 3)


def stop():
    ac.stop()
