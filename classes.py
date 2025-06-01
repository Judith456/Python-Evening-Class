"""
#create a class named car with property x
class Car:
    x = 5

#Create an object named p1, and print the value of x:
p1 = Car()
print(p1.x)

#class person with name and age properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(f"I am p1.age years")
print("I am", p1.age, "years")
"""

"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)   # gives an error its suposed t be p1.name or p1.age



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)    #it does not bring an error


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("I am", self.age)

p1 = Person("John", 36)
p1.myfunc()

#Can use thers words other than self
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
"""



