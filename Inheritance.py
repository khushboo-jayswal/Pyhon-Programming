class vehicals:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def getName(self):
        print(self.name)
    def getColor(self):
        print(self.color)
    def getModel(self):
        print(self.model)

class car(vehicals):
    def __init__(self):
        super().__init__("Audi", "White", "VDI")
    def getDescription(self):
        print(self.name, self.color, self.model)
c = car()
c.getDescription()
c.getName()
c.getColor()
c.getModel()