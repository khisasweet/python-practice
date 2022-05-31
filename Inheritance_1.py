class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    
  def __str__(self):
    return self.name + ' is a ' + self.breed

pet1 = Dog("Max", "Labrador")
print(pet1)

