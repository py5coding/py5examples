"""
/**
* ControlP5 Textfield
*
*
* find a list of public methods available for the Textfield Controller
* at the bottom of this sketch.
*
* by Andreas Schlegel, 2012
* www.sojamo.de/libraries/controlp5
*
*/
"""
add_library('controlP5')


class TextListener(ControlListener):

    def control_event(self, e):
        print('%s -> %s' % (e.get_name(), e.get_string_value()))


def setup():
    size(700, 400)
    font = create_font("sansserif", 20)
    global cp5
    cp5 = ControlP5(this)

    cp5.add_textfield("input").set_position(20, 100).set_size(
        200, 40).set_font(font).set_focus(True).set_color(color(255, 0, 0))

    cp5.add_textfield("textValue").set_position(20, 170).set_size(
        200, 40).set_font(create_font("arial", 20)).set_auto_clear(False)

    cp5.add_bang("clear").set_position(240, 170).set_size(
        80, 40).get_caption_label().align(ControlP5.CENTER, ControlP5.CENTER)

    cp5.add_textfield("default").set_position(20, 350).set_auto_clear(False)

    text_font(font)

    # You can use a lambda as a callback...
    cp5.get_controller("input").add_listener(
        lambda e: print('%s -> %s' % (e.get_name(), e.get_string_value())))
    # Or you can use a class that implements the ControlP5 callback
    # interface...
    cp5.get_controller("textValue").add_listener(TextListener())
    cp5.get_controller("default").add_listener(TextListener())
    # Or you can use a function.

    def listen_to_clear(e):
        if e.get_action() == ControlP5.ACTION_RELEASED:
            clear()
    cp5.add_callback(listen_to_clear)


def draw():
    background(0)
    fill(255)
    text(cp5.get(Textfield, "input").get_text(), 360, 130)
    text(cp5.get(Textfield, "textValue").get_text(), 360, 180)


def clear():
    cp5.get(Textfield, "textValue").clear()
