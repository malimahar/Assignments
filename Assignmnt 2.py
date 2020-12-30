#NUMBERS
#TYPE
a= 5
b = 4.5
c = "wizinsights"
d = 8j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
m = float(a)
#RANDOM NUMBERS
import random
print(random.randrange(3,5))
#Tuples
std_name = ("Gull", "Ali", "Fatima", "haseeb", "mujeeb")
Fruits = ("orange", "banana", "apple", "grapes")
print(std_name)
print(type(std_name))
print(len(std_name))
print(std_name[1])
print(std_name[-2])
print(std_name[2:4])
b = list(std_name)
b[2:4] = "pea", "cabbage"
std_name = tuple(b)
print(std_name)
b.append("tomato")
std_name = tuple(b)
print(std_name)
b.remove("cabbage")
std_name = tuple(b)
print(std_name)
# unpacking of tuple
print("onion")
print("potato")
print("tomato")
print("pepper")
print("carrot")
# Joining and multiplying of tuples
print(std_name + Fruits)
print(std_name*3)
# delete std_name -> print(std_name) tuple is deletd due to it causes an error.
#Lists.
my_list = [11, 16, 3, 7, 9, "lhr", "fsd", "Multan","sukkur"]
a_list = [True, False, False, True]
print(my_list)
# Check length of list
print(len(my_list))
# Access list's items
print(my_list[:6])
print(my_list[3:])
print(my_list[4:9])
print(my_list[-6:-3])
# Sort list
a_list.sort()
print(a_list)
a_list.sort(reverse=True)
print(a_list)
# Add items
my_list.append("lhr")
print(my_list)
my_list.insert(3, "fsd")
print(my_list)
my_list.extend(a_list)
print(my_list)
# Joining of lists
print(a_list + my_list)
my_list.extend(a_list)
print(my_list)
# Remove item from list
my_list.remove("Multan")
print(my_list)
del my_list[4]
print(my_list)
# pop method also used to remove a specific item from list.
my_list.pop()
print(my_list)
# Check index
print(my_list.index("lhr"))
# Change item of list
my_list[1:3] = ["lhr", "sukkur"]
print(my_list)
# Check type of list
print(type(my_list))
# Copy list
my_list = a_list.copy()
print(my_list)
my_list = list(a_list)
print(my_list)
#Dictionary
country_code = {"pakistan": 250, "india": 300,
                "USA": 700, "UK": 500, "Europe": 90}
print(country_code["USA"])
# Check keys of dictionary
print(country_code.keys())
# Check type of dictionary
print(type(country_code))
# Change dictionary
country_code["USA"] = 10
print(country_code)
# Update dictionary
country_code.update({"UK": 15})
print(country_code)
# delete method remove a specific item and also removes the whole dictionary this will cause an error
del (country_code["india"])
print(country_code)
country_code.pop("USA")
print(country_code)
country_code.popitem()
print(country_code)
# remove items from dictionary
country_code.clear()
print(country_code)
