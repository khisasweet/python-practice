a =[x for x in range(10) if x % 2 == 0]
print(a)
b = list(filter(lambda x:x%2 == 0, [x for x in range(10)]))
print(b)
c = [1 if x % 2 == 0 else 0 for x in range(5)]
print(c)
d = list(map(lambda x: 1 if x%2 == 0 else 0, [x for x in range(5)]))
print(d)
mix_list = [1, "Python", 0.5, "Apple", 3.0, "\n"]
numbers = list(filter(lambda x: isinstance(x, float) or isinstance(x, int),  mix_list))
print(numbers)
