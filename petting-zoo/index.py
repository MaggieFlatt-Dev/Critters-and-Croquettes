# Import each animal from category
from slithering import Boa, Chameleon, Copperhead, Gecko, RatSnake
from swimming import Frog, Goldfish, Mallard, Newt, Turtle
from walking import Donkey, Goat, Llama, Pig, Sheep


miss_fuzz = Llama("Miss Fuzz", "mammal", "morning", "Llama Chow")
miss_fuzz.feed()
print(miss_fuzz)

donkey = Donkey("donkey", "mammal", "midday", "carrots")
donkey.feed()
print(donkey)
# print(f"{donkey.name} the {donkey.species} is available to pet during the {donkey.shift} shift.")
babe = Pig("Babe", "mammal", "afternoon", "Corn Feed")
babe.feed()
print(babe)

carl = Sheep("Carl", "mammal", "morning", "Clover")
carl.feed()
print(carl)

robert = Goat("Robert", "mammal", "afternoon", "Alfalfa")
robert.feed()
print(robert)
# goldie = Goldfish("Goldie", "fish")
# mark = Mallard("Mark", "fowl")
hopalong = Frog("Hopalong", "amphibian")
print(hopalong)
# stewart = Newt("Stewart", "amphibian")
# hank = Turtle("Hank", "reptile")
# hiss = Copperhead("Hiss", "reptile")
# rachel = RatSnake("Rachel", "reptile")
# charles = Gecko("Charles", "reptile")
pooh = Boa("Pooh", "reptile")
print(pooh)
# sarah = Chameleon("Sarah", "reptile")