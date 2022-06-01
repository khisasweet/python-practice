class Super:
    # Add your code here
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    # Add your code here
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)
