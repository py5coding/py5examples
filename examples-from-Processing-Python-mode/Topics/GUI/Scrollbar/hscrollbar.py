class HScrollbar(object):

    def __init__(self, xpos, ypos, s_width, s_height, loosetemp):
        # width and height of bar
        self.s_width = s_width
        self.s_height = s_height
        widthtoheight = s_width - s_height
        self.ratio = float(s_width) / float(widthtoheight)
        # x and y position of bar
        self.xpos = xpos
        self.ypos = ypos - self.s_height / 2
        self.spos = self.xpos + self.s_width / 2 - self.s_height / 2
        self.newspos = self.spos
        self.spos_min = self.xpos
        self.spos_max = self.xpos + self.s_width - self.s_height
        self.loose = loosetemp
        # is the mouse over the slider?
        self.over = False
        self.locked = False

    def update(self):
        self.over = self.over_event()
        self.locked = mouse_pressed and self.over
        if self.locked:
            self.newspos = constrain(mouse_x - self.s_height / 2,
                                     self.spos_min, self.spos_max)
        if abs(self.newspos - self.spos) > 1:
            self.spos = self.spos + (self.newspos - self.spos) / self.loose

    def over_event(self):
        return (self.xpos < mouse_x < self.xpos + self.s_width
                and self.ypos < mouse_y < self.ypos + self.s_height)

    def display(self):
        no_stroke()
        fill(204)
        rect(self.xpos, self.ypos, self.s_width, self.s_height)
        if self.over or self.locked:
            fill(0, 0, 0)
        else:
            fill(102, 102, 102)
        rect(self.spos, self.ypos, self.s_height, self.s_height)

    def get_pos(self):
        # Convert spos to be values between
        # 0 and the total width of the scrollbar
        return self.spos * self.ratio
