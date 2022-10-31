from l_system import LSystem


class PentigreeLSystem(LSystem):

    def __init__(self):
        self.steps = 0
        self.somestep = 0.1
        self.xoff = 0.01
        self.axiom = "F-F-F-F-F"
        self.rule = "F-F++F+F-F-F"
        self.start_length = 60.0
        self.theta = radians(72)
        self.reset()

    def use_rule(self, r_):
        self.rule = r_

    def use_axiom(self, a_):
        self.axiom = a_

    def use_length(self, l_):
        self.start_length = l_

    def use_theta(self, t_):
        self.theta = radians(t_)

    def reset(self):
        self.production = self.axiom
        self.draw_length = self.start_length
        self.generations = 0

    def get_age(self):
        return self.generations

    def render(self):
        translate(width / 4, height / 2)
        self.steps += 3
        if self.steps > len(self.production):
            self.steps = len(self.production)

        for i in range(self.steps):
            step = self.production[i]
            if step == 'F':
                no_fill()
                stroke(255)
                line(0, 0, 0, -self.draw_length)
                translate(0, -self.draw_length)
            elif step == '+':
                rotate(self.theta)
            elif step == '-':
                rotate(-self.theta)
            elif step == '[':
                push_matrix()
            elif step == ']':
                pop_matrix()
