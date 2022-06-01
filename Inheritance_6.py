class ClassA:
    def fun(self):
        print("fun from ClassA")
    def coolmethod(self):
        return self.fun()

class ClassB(ClassA):
    def fun(self):
        print("fun from ClassB")

new_value = ClassB()

new_value.coolmethod()
