class cars:
    carCount = 0
    def __init__(self, color, model):
        self.color = color
        self.model = model
        cars.carCount += 1
    def displayCarCount(self):
        print("Total count of cars are %d" % cars.carCount)
    def showColorBrand(self):
        print("The color and Brand of the Car is: ", self.color, self.model)
car1 = cars("Black", "BMW")
car2 = cars("Orange", "Duster")
car1.showColorBrand()
car2.displayCarCount()

class Greetings:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print("Greeting Deleterd")
    def SayHi(self):
        print("Hello", self.name)
x1 = Greetings("Vishvesh")
x2 = x1
del x2