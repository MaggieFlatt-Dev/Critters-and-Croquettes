from swimming.pond import Pond

class Frog(Pond):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Pond"

   def __str__(self):
      return f"{self.name} is a {self.species}"