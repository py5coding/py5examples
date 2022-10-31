# Class for animating a sequence of GIFs
class Animation(object):

    def __init__(self, image_prefix, count):
        self.frame = 0
        self.image_count = count
        self.images = [Py5Image] * self.image_count
        for i in range(self.image_count):
            # Use nf() to number format 'i' into four digits
            filename = image_prefix + nf(i, 4) + ".gif"
            self.images[i] = load_image(filename)

    def display(self, xpos, ypos):
        self.frame = (self.frame + 1) % self.image_count
        image(self.images[self.frame], xpos, ypos)

    def get_width(self):
        return self.images[0].width
