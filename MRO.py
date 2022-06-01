### Module Resulution Order ####
## The way that a programming language scans through the upper part of a class's hierarchy 
### in order to find the entity it currently needs

class ClassA:
  def top(self):
    print("In ClassA")
class ClassB(ClassA):
  def middle(self):
    print("In ClassB")
class ClassC(ClassA):
  def middle(self):
    print("In ClassC")
class ClassD(ClassB, ClassC):
  def bottom(self):
    print("In ClassD")
object = ClassD()


    
    
    
    
    
