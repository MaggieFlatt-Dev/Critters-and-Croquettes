from animal import Animal

class Pond(Animal):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.swimming = True