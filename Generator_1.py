
### Generator is a
### Specialized code that's able to return a series of values, and to control the iteration process

class CustomRange:
  def __init__(self, range):
    self.__range =range
    self.__i = 0
    
  def __iter__(self):
    return self

  def __next__(self):
    res = self.__i
    self.__i += 1
    print("res: ", str(res))
    if self.__i > self.__range:
      raise StopIteration
    return res 
    
r = CustomRange(10)

print(r.__next__())
print(r.__next__())
print(r.__next__())
