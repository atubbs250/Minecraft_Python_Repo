class Cat(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

fluff = Cat("Fluff", 4.5)
fluff.weight = 5

print(fluff.weight)
