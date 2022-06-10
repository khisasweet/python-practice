### The map() function executes a specified function for each item in an iterable. 
### The item is sent to the function as a parameter.
### map(function, iterables) 

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry')) 
