#----------------------->try and except<-----------------
# Exception handling
try:
        print(x)
except:
        print("An exception occurred")

#The try block will generate an exception, because x is not defined
# many exceptions
try:
  print(a)
except NameError:
  print("Variable a is not defined") # NameError occurs when variable is not defined.
except:
  print("Something else went wrong")
# else
try:
  print("somtehing  done wrong")
except:
  print("Something went wrong")
else:
  print("Everything is right")
#------------------>finally<---------------------
try:
  print("somtehing  done wrong")
except:
  print("Something went wrong")
else:
  print("Everything is right")
finally:
  print("Finally ignore all steps like try except ")
#--------------->raise<---------------------
# raise keyword is used to raised an exception
x ="Ali"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

