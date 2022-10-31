class Handle(object):

    def __init__(self, x, y, stretch, size, others):
        self.x = x
        self.y = y
        self.stretch = stretch
        self.size = size
        self.box_x = self.x + self.stretch - self.size / 2
        self.box_y = self.y - self.size / 2
        self.others = others
        self.over = False
        self.press = False
        self.locked = False
        self.others_locked = False

    def update(self):
        self.box_x = self.x + self.stretch
        self.box_y = self.y - self.size / 2

        self.others_locked = False
        for handle in self.others:
            if handle.locked:
                self.others_locked = True
                break
        if not self.others_locked:
            self.over_event()
            self.press_event()
        if self.press:
            self.stretch = constrain(mouse_x - width / 2 - self.size / 2,
                                     0, width / 2 - self.size - 1)

    def over_event(self):
        self.over = over_rect(self.box_x, self.box_y, self.size, self.size)

    def press_event(self):
        if self.over and mouse_pressed or self.locked:
            self.press = True
            self.locked = True
        else:
            self.press = False

    def release_event(self):
        self.locked = False

    def display(self):
        line(self.x, self.y, self.x + self.stretch, self.y)
        fill(255)
        stroke(0)
        rect(self.box_x, self.box_y, self.size, self.size)
        if self.over or self.press:
            line(self.box_x, self.box_y,
                 self.box_x + self.size, self.box_y + self.size)
            line(self.box_x, self.box_y + self.size,
                 self.box_x + self.size, self.box_y)


def over_rect(x, y, width, height):
    return x <= mouse_x <= x + width and y <= mouse_y <= y + height
