# Python Conditions and If statements
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
#if statment
a = 33
b = 200
if b > a:
  print("b is greater than a")
#Elif statement
a = 23
b = 23
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
#else statment
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
#Short hand If statement
if a > b:
    print("a is greater than b")
 #Short hand If, Else statement
a = 2
b = 330
print("A") if a > b else print("B")
# If with And opreator
a = 300
b = 38
c = 400
if a > b and c > a:
    print("Both conditions are True")
    # If with Or opreator
    a = 500
    b = 45
    c = 600
    if a > b or a > c:
        print("At least one of the conditions is True")
 # Nested If statement
        x = 30
        if x > 10:
            print("Above ten,")
            if x > 20:
                print("and also above 20!")
            else:
                print("but not above 20.")
    # The pass Statement
    a = 33
    b = 200
    if b > a:
        print("pass")
#The while loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break           # break statement
    i += 1
#for loop
    students = ["ali", "gull", "haseeb"]
    for x in students:
        if x == "haseeb":
            break
        print(x)

    #range function
   # range(start, stop, increment)
x = range(3, 20, 1)

for n in x:
  print(n)
#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
