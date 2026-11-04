# Tuple are enclosed in curve brackets and List are enclosed in square brackets

tp = ("apple", "bannnana", "2", "fog", "true", "false", "354.67") 
print(type(tp)) 
li = ["apple", "bannnana", "2", "fog", "true", "false", "354.67"]
print(type(li))

# Tuples are Immutable like Strings (It does not support item assigment)

tp = ("apple", "bannnana", "2", "fog", "true", "false", "354.67")
tp[0] = "Muzamil"
print(tp)

# Empty tuple 

a = ()
print(type(a))

# Single Variable Tuple 

b = (3,) # Comma is important so that the python interpreter to understand that it is single
                     #   variable tuple or the output will be int type 
print(type(b))
c = (3)
print(type(c))