# Add 10 to argument `a`, and return the result
x = lambda a: a + 10
print(x(5))  # Output: 15

# Multiply argument `a` with argument `b` and return the result
x = lambda a, b: a * b
print(x(5, 6)) 

# Summarize argument `a`, `b`, and `c` and return the result
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))  

# Use lambda as an anonymous function inside another function
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11)) 

# Use the same function definition to create a function that triples the number
def myfunc(n):
    return lambda a: a * n

mytripler = myfunc(3)
print(mytripler(11)) 

# Create both doubling and tripling functions in the same program
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))  
print(mytripler(11)) 
