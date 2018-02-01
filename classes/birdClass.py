class Bird(object):
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def birdcall(self):
        print("chirp")

    def fly(self):
        print("flap")

class Penguin(Bird):
    def swim(self):
        print("swimming")
        

gardenBird = Bird("Geoffrey", 12)
gardenBird.birdcall()
gardenBird.fly()

sarahThePenguin = Penguin("Sarah", 10)
sarahThePenguin.swim()
sarahThePenguin.fly()
sarahThePenguin.birdcall()


