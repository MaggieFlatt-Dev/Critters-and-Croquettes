from walking.petting_area import PettingArea

class Sheep(PettingArea):

   def __init__(self, name, species, shift):
    super().__init__(name, species)
    self.area = "Petting Area"
    self.area = shift