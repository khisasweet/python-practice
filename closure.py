# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. 

# Python program to illustrate
# closures
def outerFunction(text):
    text = text
 
    def innerFunction():
        print(text)
 
    # Note we are returning function
    # WITHOUT parenthesis
    return innerFunction 
 
if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()
