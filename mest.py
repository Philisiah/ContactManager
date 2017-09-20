class School:

    def __init__(self, name):
        self.name = name


class EIT:

    def __init__(self, name, nationality, fun_fact=[]):
        self.name = name
        self.nationality = nationality
        self.fun_fact = fun_fact

    def fun_fact(self):
        return self.fact


class Fellow:

    def __init__(self, name, nationality, happiness_level=0):
        self.name = name
        self.nationality = nationality
        self.happiness_level = happiness_level

    def teach(self):
        return self.happiness_level -= 1

    def eat(self):
        return self.happiness_level += 1
