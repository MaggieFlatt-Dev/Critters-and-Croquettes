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
