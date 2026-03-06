from animal import Animal

class GlassTank(Animal):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.slithering = True