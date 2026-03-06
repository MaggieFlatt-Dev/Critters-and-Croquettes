# # Import the python datetime module to help us create a timestamp
# from datetime import date

# class Llama:

#   def __init__(self):
#     # Establish the properties of each animal 
#     # with a default value
#     self.name = ""
#     self.species = ""
#     self.date_added = date.today()

# miss_fuzz = Llama()
# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "domestic llama"

# for prop, value in vars(miss_fuzz).items():
#   print(f"{prop}:")
#   print(f"{value}\n")

# Classy Critters Collection 
# Create 15 classes for representing critters from Bobby's Petting Zoo
from datetime import date

class Animal:

  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()

class PettingArea(Animal):

  def __init__(self, name, species):
    super().__init__(name, species)
    self.walking = True

class GlassTank(Animal):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.slithering = True

class Pond(Animal):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.swimming = True

class Donkey(PettingArea):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Petting Area"

class Llama(PettingArea):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Petting Area"

class Goat(PettingArea):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Petting Area"

class Pig(PettingArea):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Petting Area"

class Sheep(PettingArea):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Petting Area"

class Goldfish(Pond):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Pond"

class Mallard(Pond):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Pond"

class Frog(Pond):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Pond"

class Newt(Pond):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Pond"

class Turtle(Pond):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Pond"

class Copperhead(GlassTank):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Glass Tank"

class RatSnake(GlassTank):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Glass Tank"

class Gecko(GlassTank):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Glass Tank"

class Boa(GlassTank):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Glass Tank"

class Chameleon(GlassTank):

   def __init__(self, name, species):
    super().__init__(name, species)
    self.area = "Glass Tank"


# Create 1 instance for each class
donkey = Donkey("donkey", "mammal")

miss_fuzz = Llama("Miss Fuzz", "mammal")

babe = Pig("Babe", "mammal")

carl = Sheep("Carl", "mammal")

robert = Goat("Robert", "mammal")

goldie = Goldfish("Goldie", "fish")

mark = Mallard("Mark", "fowl")

hopalong = Frog("Hopalong", "amphibian")

stewart = Newt("Stewart", "amphibian")

hank = Turtle("Hank", "reptile")

hiss = Copperhead("Hiss", "reptile")

rachel = RatSnake("Rachel", "reptile")

charles = Gecko("Charles", "reptile")

pooh = Boa("Pooh", "reptile")

sarah = Chameleon("Sarah", "reptile")
