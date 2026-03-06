from walking.petting_area import PettingArea


class Llama(PettingArea):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Petting Area"