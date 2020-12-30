#*********methods********#
class Person:
    def __init__(self, name, age):  # Init function it works like constructor
        self.name = name
        self.age = age

    def myfunc(self):  # Method
        print("Hello my name is " + self.name)
        print("My age is ", self.age)

p1 = Person("Muhammad Ali ", 31)  # Object of class
p1.myfunc()  # object called by method
#nested if statement
n=35
if n > 30:
    print("Entered number also above 30!")
    if n > 20:
        print("Entered number also above 20!")
    else:
        print("Entered number less then 20.")
# Nested For loop
col = ["red", "yellow", "green"]
fruits = ["apple", "banana", "mango"]
for x in col:
    for y in fruits:
        print(x, y)

#Lambda expressions
#lambda with simple parameter
x = lambda a: a + 10
print(x(5))
#Sum all argument a, b, and c and return the result
x = lambda a, b, c : a + b + c
print(x(9, 1, 2))
#lambda use  function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(15))
print(mytripler(14))
#***********function**********
#call with arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("ali", "mahar")
#Arbaitry arguments
def my_function(child1, child2, child3):
  print("The youngest child is " + child1)

my_function(child1 = "gull", child2 = "kaleem", child3 = "Ali")
#default parameter
def in_function(country = "Iran"):
  print("I am from " + country)
in_function("Turkey")
in_function("Pakistan")
in_function()
in_function("china")
#passing list arguments
def my_func(fruits):
  for x in fruits:
    print(x)

fruits = ["apple", "banana", "mango","Orange", "lemon", "watermelon"]

my_func(fruits)
#return values
def my_func1(x):
  return 7 * x

print(my_func1(6))
print(my_func1(8))
print(my_func1(10))



