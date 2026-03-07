from walking.petting_area import PettingArea
from datetime import date

class Llama(PettingArea):

   def __init__(self, name, species, shift, food):
      super().__init__(name, species)
      self.area = "Petting Area"
      self.shift = shift
      self.food = food

   def feed(self):
      print(f"{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}")

   def __str__(self):
      return f"{self.name} is a {self.species}"