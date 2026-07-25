class Dog:
    species = "Canis familiaris"  # class attribute — shared across ALL instances

    def __init__(self, name):
        self.name = name  # instance attribute — unique per object

d1 = Dog("Rex")
d2 = Dog("Max")
print(d1.species, d2.species)  # both "Canis familiaris" — same object in memory
Dog.species = "Wolf"           # changes for ALL instances
print(d1.species)              # "Wolf"

d1.species = "Special Dog"     # this creates a NEW instance attribute on d1 only
print(d1.species, d2.species)  # "Special Dog" "Wolf" — d2 untouched