class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.cost, self.cost)

    def get_age(self):
        return 2016 - self.year

    def is_vintage(self):
        return self.get_age() > 50
