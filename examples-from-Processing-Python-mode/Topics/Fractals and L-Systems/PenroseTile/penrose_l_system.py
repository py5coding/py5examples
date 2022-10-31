from l_system import LSystem


class PenroseLSystem(LSystem):

    def __init__(self):
        self.axiom = "[X]++[X]++[X]++[X]++[X]"
        self.rule = ""
        self.steps = 0
        self.rule_w = "YF++ZF4-XF[-YF4-WF]++"
        self.rule_x = "+YF--ZF[3-WF--XF]+"
        self.rule_y = "-WF++XF[+++YF++ZF]-"
        self.rule_z = "--YF++++WF[+ZF++++XF]--XF"
        self.start_length = 460.0
        self.theta = radians(36)
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
        translate(width / 2, height / 2)
        pushes = 0
        repeats = 1
        self.steps += 12
        if self.steps > len(self.production):
            self.steps = len(self.production)

        for i in range(self.steps):
            step = self.production[i]
            if step == 'F':
                stroke(255, 60)
                for j in range(repeats):
                    line(0, 0, 0, -self.draw_length)
                    no_fill()
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
                pushes += 1
                push_matrix()
            elif step == ']':
                pop_matrix()
                pushes -= 1
            # Use ord to get ASCII value of letter
            elif (ord(step) >= 48) and (ord(step) <= 57):
                repeats = ord(step) - 48
        while pushes > 0:
            pop_matrix()
            pushes -= 1

    def iterate(self, prod_, rule_):
        new_production = ""
        for i in range(len(prod_)):
            step = self.production[i]
            if step == 'W':
                new_production = new_production + self.rule_w
            elif step == 'X':
                new_production = new_production + self.rule_x
            elif step == 'Y':
                new_production = new_production + self.rule_y
            elif step == 'Z':
                new_production = new_production + self.rule_z
            elif step != 'F':
                new_production = new_production + step
        self.draw_length = self.draw_length * 0.5
        self.generations += 1
        return new_production
