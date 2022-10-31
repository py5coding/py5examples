class LSystem(object):

    def __init__(self):
        self.steps = 0

        self.axiom = "F"
        self.rule = "F+F-F"
        self.start_length = 90.0
        self.theta = radians(120.0)
        reset()

    def reset(self):
        self.production = axiom
        self.draw_length = start_length
        self.generations = 0

    def get_age(self):
        return generations

    def render(self):
        translate(width / 2, height / 2)
        steps += 5
        if steps > len(production)():
            steps = len(production)()

        for i in range(steps):
            step = production.char_at(i)
            if step == 'F':
                rect(0, 0, -draw_length, -draw_length)
                no_fill()
                translate(0, -draw_length)
            elif step == '+':
                rotate(theta)
            elif step == '-':
                rotate(-theta)
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
        new_production = new_production.replace("F", rule_)
        return new_production
