### Program to print square of numbers from 1 to n
def num_generator(n):
    num =1
    while True:
      yield num
      if num == n:
         return
      else:
         num += 1
s = num_generator(20)
print (s.__next__())
print (s.__next__())
print (s.__next__())
