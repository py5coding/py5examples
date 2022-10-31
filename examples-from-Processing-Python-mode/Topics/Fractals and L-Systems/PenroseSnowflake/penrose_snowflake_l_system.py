from l_system import LSystem


class PenroseSnowflakeLSystem(LSystem):

    def __init__(self):
        self.axiom = "F3-F3-F3-F3-F"
        self.rule = ""
        self.steps = 0
        self.rule_f = "F3-F3-F45-F++F3-F"
        self.start_length = 450.0
        self.theta = radians(18)
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
        translate(width, height)
        repeats = 1
        self.steps += 3
        if self.steps > len(self.production):
            self.steps = len(self.production)
        for i in range(self.steps):
            step = self.production[i]
            if step == 'F':
                for j in range(repeats):
                    line(0, 0, 0, -self.draw_length)
                    translate(0, -self.draw_length)
                repeats = 1
            elif step == '+':
                for j in range(repeats):
                    rotate(self.theta)
                repeats = 1
            elif step == '-':
                for j in range(repeats):
                    rotate(-self.theta)
                repeats = 1
            elif step == '[':
                push_matrix()
            elif step == ']':
                pop_matrix()
            # Use ord to get ASCII value of letter
            elif 48 <= ord(step) <= 57:
                repeats += ord(step) - 48

    def iterate(self, prod_, rule_):
        new_production = ""
        for i in range(len(prod_)):
            step = self.production[i]
            if step == 'F':
                new_production = new_production + self.rule_f
            elif step != 'F':
                new_production = new_production + step

        self.draw_length = self.draw_length * 0.4
        self.generations += 1
        return new_production
