def my_friends():
    print("Mujeeb", "Ali", "Haseeb")
my_friends()
#by passing arguments
def my_friends(fname):
    print(fname + " " +"is my friend.")
my_friends("Mujeeb")
my_friends("Ali")
my_friends("Haseeb")
#call the function with 2 arguments.
def my_friends(fname, lname,thirdname):
    print(fname+" "+lname+" ")
my_friends("Mujeeb", "Haseeb",)
my_friends("Ali", "Mahar",)
my_friends("gull", "Hassan",) #If we try to call the function with 1 or 3 arguments, we will get an error:
#By passing Arbitrary Keyword Arguments, (**kwargs)
# function will recieve dictionary argument
def my_friends(**friend):
    print("My last name is" + " "+ friend["lname"])
my_friends(fname="Ali", lname="Mahar")
# by passing Arbitrary Arguments, (*args) ....*args access item accordingly
# function will recieve tuple arguments
def my_friends(*friend):
    print("My best friend is" + " " + friend[1])

#Keyword Arguments
#we can also send arguments with the key = value syntax.
def my_friends(f1, f2, f3,f4):
  print("My best friend is " + f4)
my_friends(f1="Ali", f2="gulu", f3="saifi",f4="samiullah")
#default parameter value
def my_friends(city = "DG khan"):
  print("I am from " + city)
my_friends("karachi")
my_friends("Sukkur")
my_friends()
my_friends("Lahore")
#Passing a List as an Argument
def my_friends(veg):
    for x in veg:
        print(x)
veg = ["onion", "carrots", "pototo"]
my_friends(veg)
# return values
def my_friends(number):
    return 5 *number
print(my_friends(4))
print(my_friends(5))
print(my_friends(6))
#pass statement
def my_friends():
     pass   #if function with no content put the pass statement to avoid getting error
#---------------------------->Recursive function<------------------------
# the benefit of recursion is that we can loop through data to reach a result.
def tri_recursion(x):
  if(x >= 0):
    result = x + tri_recursion(x - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
#-------------------------->Methods<---------------------------
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def my_friend(self):
    print("Hello my name is " + self.name)

p1 = Person("ALi",35)
p1.my_friend()
#modify object properties
p1.age = 35
print(p1.age)
# delete object properties
#del p1.age
#print(p1.age) ........it causes error because there' no more p1 value

#delete objects.........it causes error because there' no more p1 value
#del p1
#print(p1)
# pas statement
class Person:
    pass