from swimming.pond import Pond

class Turtle(Pond):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Pond"