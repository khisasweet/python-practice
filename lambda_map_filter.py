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


mix_list = [1, "Python", 0.5, "Apple", 3.0, "\n"]
numbers = list(filter(
    lambda n: isinstance(n, float) or isinstance(n, int), mix_list
    ))

print(numbers)

events = [
        {'date': 11212021, 'name': 'Bengali wedding'},
        {'date': 11012021, 'name': 'Project meeting'},
        {'date': 11112021, 'name': 'Guitar class'},
]

# Add the sorted code here
sorted_events = sorted(events, key=lambda x: x['date'])
print(sorted_events)

# Create the counter generator
def counter(n):
    i = 0
    while i <= n:
        yield i
        i += 1

c = counter(3)
print(next(c), next(c), next(c), next(c), next(c))
