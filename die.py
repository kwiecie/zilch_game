from random import randint

class Die:
    def __init__(self, value=None, sides=6):
        self.sides = sides
        if type(value) == int:
            self.value = value
        else:
            self.value = self.roll()

    def __repr__(self):
        return str(self.value)

    def __eq__(self, die_to_compare):
        if self.get_value() == die_to_compare:
            return 0
        elif self.get_value() > die_to_compare:
            return 1
        else:
            return -1

    def __lt__(self, die_to_compare):
        if self.get_value() == die_to_compare:
            return 0
        elif self.get_value() > die_to_compare:
            return 1
        else:
            return -1

    def __gt__(self, die_to_compare):
        if self.get_value() == die_to_compare:
            return 0
        elif self.get_value() > die_to_compare:
            return 1
        else:
            return -1

    def roll(self):
        self.value = randint(1, self.sides)
        return self.value

    def get_value(self):
        return self.value

    def get_num_of_sides(self):
        return self.sides

