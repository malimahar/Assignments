#Arithmetic operators
a = 2
print(a+a)
print(a-a)
print(a*a)
print(a/a)
print(a%a)
print(a**a)
print(a//a)
#Assignment operators
a = 5
print(a)
#a = a+2 same for all
a += 2
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)
a %= 2
print(a)
a = 5
a **= 2
print(a)
a //= 2
print(a)
#Bitewise operators
a = 5
a &= 2
print(a)
a = 5
a |= 2
print(a)
a = 5
a ^= 2
print(a)
a = 5
a >>= 2
print(a)
a = 5
a <<= 2
print(a)
#Logical Operators
print(a<=a and a>=a)
print(a==a or a>a)
print(not(a<=a and a>=a))
#Identity Operatos
veg = ["potota", "carrot", "onion"]
x = veg
print(x is veg)
print(x is not veg)
#Membership Operators
print("potato" in veg)
print("onion" not in veg)
#   Comparison Operators
a = 6
print(a==a)
print(a!=a)
print(a>a)
print(a<a)
print(a>=a)
print(a<=a)
# ---------------------------->Conditional Expressions<---------------------------
a = 15
b = 20
if a>=b:
    print("a is greater than b")
else:
    print("b is greater than a")
#----------------------------->Chained Operators<-------------------------------
a = 38
b = 65
c = 15
print(a<b<c)
print(a<=b<=c)
print(a<b*c/a%b//c)