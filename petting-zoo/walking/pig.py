from walking.petting_area import PettingArea

class Pig(PettingArea):

   def __init__(self, name, species, shift):
    super().__init__(name, species)
    self.area = "Petting Area"
    self.shift = shift