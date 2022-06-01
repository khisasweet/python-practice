class ClassA:
    number = 100
    def multiply(self,amount):
        print(self.number * amount)

class ClassB(ClassA):
    number = 200
    def multiply(self,amount):
        print(self.number * amount)

my_instance = ClassB()
print(my_instance.number)
print(my_instance.multiply(2))
