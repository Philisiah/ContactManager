import csv
class School:

    def __init__(self, eits, fellows):
        self.eits = eits
        self.fellows = fellows


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
        self.happiness_level -= 1

    def eat(self):
        self.happiness_level += 1

with open('eits.csv', 'r') as file:
	nationalities = ['Ghana', 'Kenya', 'Nigeria', 'South Africa', 'Ivory Coast']	
	for line in csv.reader(file):
		for name in line:
			if name in nationalities:
				print (line)

