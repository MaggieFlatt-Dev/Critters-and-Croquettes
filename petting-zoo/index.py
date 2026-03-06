# Import each animal from category
from slithering import Boa, Chameleon, Copperhead, Gecko, RatSnake
from swimming import Frog, Goldfish, Mallard, Newt, Turtle
from walking import Donkey, Goat, Llama, Pig, Sheep


donkey = Donkey("donkey", "mammal", "midday")
print(f"{donkey.name} the {donkey.species} is available to pet during the {donkey.shift} shift.")
# miss_fuzz = Llama("Miss Fuzz", "mammal", "morning")
# babe = Pig("Babe", "mammal", "afternoon")
# carl = Sheep("Carl", "mammal", "morning")
# robert = Goat("Robert", "mammal", "afternoon")
# goldie = Goldfish("Goldie", "fish")
# mark = Mallard("Mark", "fowl")
# hopalong = Frog("Hopalong", "amphibian")
# stewart = Newt("Stewart", "amphibian")
# hank = Turtle("Hank", "reptile")
# hiss = Copperhead("Hiss", "reptile")
# rachel = RatSnake("Rachel", "reptile")
# charles = Gecko("Charles", "reptile")
# pooh = Boa("Pooh", "reptile")
# sarah = Chameleon("Sarah", "reptile")