from slithering.glass_tank import GlassTank

class RatSnake(GlassTank):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Glass Tank"