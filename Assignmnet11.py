#using map function
def friend(a, b):
  return a + b

x = map(friend, ('ali', 'gull', 'Saqib'), ('mahar', 'hassan', 'Zain'))

print(x)

#convert the map into a list, for readable
print(list(x))
##*********all() function*********#
#checking all function in list
mylist = [1, 1, 1]
x = all(mylist)
print(x)

# Returns true because 1 is the same as True
#checking all function in tuples
mytuple = (1, False, 1)
x = all(mytuple)
print(x)
# Returns True because both the first and the third items are True
#checking all function  in dictionery
mydict = {1 : "Apple", 2 : "Orange"}
x = all(mydict)
print(x)

# Returns true because the first key is true.

# For dictionaries the all() function checks the keys, not the values.
#check if all function in set
myset = {1, 1, 1}
x = all(myset)
print(x)
# Returns true because both the first, second  and the third items are true
#***********************any() function***************#
#checking any function in list
mylist = [1, 1, 1]
x = any(mylist)
print(x)

# Returns true because 1 is the same as True
#checking any function in tuples
mytuple = (1, False, 1)
x = any(mytuple)
print(x)
# Returns True because both the first and the third items are True
#checking any function  in dictionery
mydict = {1 : "Mango", 2 : "Orange"}
x = any(mydict)
print(x)

# Returns true because the first key is true.

# For dictionaries the any() function checks the keys, not the values.
#check if any function in set
myset = {1, 1, 1}
x = any(myset)
print(x)
# Returns true because both the first, second  and the third items are true
#***************reduce() function************#
#using reduce function
from _functools import reduce


def calculatesum(num1, num2):
    return num1 + num2


print(reduce(calculatesum, [1, 2, 3, 4,5,6,7]))
#using complex function
x = complex('5+5j')
print(x)


# defining a decorator
def mydecorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def myfunction():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
myfunction = mydecorator(myfunction)

# calling the function
myfunction()
#using enumerate
nida_friends = [0, 3, 4, 6, 7, 2]
my_friends = {False, False, 3, "gull hassan"}
print(my_friends)