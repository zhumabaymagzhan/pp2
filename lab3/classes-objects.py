# Create a class named MyClass, with a property named x
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# Create a class named Person, use the __init__() function to assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# The string representation of an object WITHOUT the __str__() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1)

# The string representation of an object WITH the __str__() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)

# Insert a function that prints a greeting, and execute it on the p1 object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Use the words mysillyobject and abc instead of self
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Set the age of p1 to 40
p1.age = 40

# Delete the age property from the p1 object
del p1.age

# Delete the p1 object
del p1

# The pass Statement
class Person:
    pass
