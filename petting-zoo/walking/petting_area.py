from animal import Animal

class PettingArea(Animal):

  def __init__(self, name, species):
    super().__init__(name, species)
    self.walking = True