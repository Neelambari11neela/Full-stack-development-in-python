"""
x = 5
y = "john"
print(x)
print(y)
"""

"""
x = 4
x = "sally"
x = 8
print(x)
"""

"""
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
"""

"""
x = 5
y = "john"
print(type(x))
print(type(y))
"""

"""
x = "python"
y = "is"
z = "awesome"
print(x,y,z)
"""

"""
def my_function(fname,lname):
    print(fname+" "+lname)
my_function("Emil","Refsnes")
"""

"""
def my_function(fname):
    print(fname+"refsnes")
my_function("emil")
my_function("tobias")
my_function("linus")
"""

"""
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)
"""

"""
class Person:
    def __init__(self, name, age):
       self.name = name
       self.age = age
p1 = Person("john",36)
print(p1.name)
print(p1.age)
"""

"""
def myfunc():
    x = 300
    print(x)
myfunc()
"""

"""
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()
"""

"""
x = 300
def myfunc():
    x= 200
    print(x)
myfunc()
print(x)
"""

"""
def myfunc():
    global x
    x = 300
myfunc()
print(x)
"""

name = input("enter your name:")
print(f"hello {name}")
