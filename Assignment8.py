#inheritence
# create parent class
class friend:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def my_friend(self):
        print(self.firstname, self.lastname)
p1 = friend("Saddam", "Hussain")
p1.my_friend()
# create child cass
class friend:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def my_friend(self):
        print(self.firstname, self.lastname)
class best_friend(friend):
    pass
p1 = best_friend("Gull", "Hassan")
p1.my_friend()
# add __init__function in child class
class friend:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def best_friend (self):
        print(self.firstname, self.lastname)
class best_friend(friend):
    def __init__(self, fname, lname):
        friend.__init__(self, fname, lname)
p1 = best_friend("Gull", "Hassan")
p1.best_friend()
#add super function
class friend:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class best_friend(friend):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.passingyear = year

x = best_friend("Gull", "Hassan", 2020)
print(x.passingyear)
#add methods
class friend:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class best_friend(friend):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.seminaryear = year

  def welcome(self):
    print("Most Welcome", self.firstname, self.lastname, "to the seminar of", self.seminaryear)

x = best_friend("Gull hassan", "Mahar", 2020)
x.welcome()
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
#***********************special function**************#
# Dunder or magic function __add__()
class my_friend:
    def __init__(self, friend):
     self.friend = friend
    def __add__(self, other):
        return self.friend + " and " + other.friend
sadam = my_friend("Saddam hussain is my friend and he is 31 years old,")
gull = my_friend("gull hassan  is my brother  and he is 21 years old.")
print(sadam+ gull)
# Dunder or magic function __mul__()
class my_friends:
    def __init__(self, friend):
     self.friend = friend
    def __mul__(self, other):
        return self.friend * other.friend
    def __eq__(self, other):
        return self.friend == other.friend
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        return self.friend < other.friend
    def __len__(self):
        return self.friend
    def __le__(self, other):
        return self.friend <= other.friend
    def __ge__(self, other):
        return self.friend >= other.friend
sadam_salary = my_friends(500)
gull_salary = my_friends(600)
print(sadam_salary * gull_salary)
print( sadam_salary== gull_salary)
print(sadam_salary != gull_salary)
print(sadam_salary < gull_salary)
print(len(sadam_salary))
print(sadam_salary <= gull_salary)
print(sadam_salary>= gull_salary)