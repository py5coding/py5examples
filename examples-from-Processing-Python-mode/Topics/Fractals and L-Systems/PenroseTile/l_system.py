class LSystem(object):

    def __init__(self):
        self.steps = 0
        self.axiom = "F"
        self.rule = "F+F-F"
        self.start_length = 190.0
        self.theta = radians(120.0)
        self.reset()

    def reset(self):
        self.production = self.axiom
        self.draw_length = self.start_length
        self.generations = 0

    def get_age(self):
        return self.generations

    def render(self):
        translate(width / 2, height / 2)
        self.steps += 5
        if self.steps > len(self.production)():
            self.steps = len(self.production)()

        for i in range(self.steps):
            step = self.production.char_at(i)
            if step == 'F':
                rect(0, 0, -self.draw_length, -self.draw_length)
                no_fill()
                translate(0, -self.draw_length)
            elif step == '+':
                rotate(self.theta)
            elif step == '-':
                rotate(-self.theta)
            elif step == '[':
                push_matrix()
            elif step == ']':
                pop_matrix()

    def simulate(self, gen):
        while self.get_age() < gen:
            self.production = self.iterate(self.production, self.rule)

    def iterate(self, prod_, rule_):
        self.draw_length = self.draw_length * 0.6
        self.generations += 1
        new_production = prod_
        new_production = new_production.replace_all("F", rule_)
        return new_production
