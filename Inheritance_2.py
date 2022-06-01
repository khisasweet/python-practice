
class Animal:
  def __init__(self, type):
    self.type = type

class Mammal(Animal):
  def __init__(self, animal):
    Animal.__init__(self, "mammal")
    self.animal = animal

  def breathe(self):
      print("Breathing...")

class Dog(Mammal):
  def __init__(self, breed):
    Mammal.__init__(self, "dog")
    self.breed = breed

  def bark(self):
      print("Woof")
      
  def __str__(self):
    return self.name + ' is a ' + self.breed

crocodile = Animal("reptile")
dolphin = Mammal("dolphin")
pet = Dog("Labrador")

print(dolphin.type)
print(dolphin.breathe())
print(pet.type)
print(pet.breathe())
print(pet.bark())

print(isinstance(pet,Dog))
print(isinstance(pet,Animal))
print(isinstance(dolphin,Dog))
print(isinstance(dolphin,Animal))
