class Cat(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def getWeightInGrams(self):
        return self.weight * 1000

    def eat(self, food):
        self.weight = self.weight + 0.05
        print(self.name + " is eating " + food)

    def eatAndSleep(self, food):
        self.eat(food)
        print(self.name + " is now sleeping...")

fluff = Cat("Fluff", 4.5)
print(fluff.weight)
fluff.eat("tuna")
fluff.eatAndSleep("tuna")
print(fluff.getWeightInGrams())
