from swimming.pond import Pond

class Mallard(Pond):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Pond"