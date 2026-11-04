a = "Muzamil" # String Slicing 
print(a[0])
print(a[6])
# print(len(a))

# Just like string, we can index in list too
list = ["apple", "bannnana", "2", "fog", "true", "false", "354.67"]
print(list[0])
print(list[6])
# print(list[7]) # Error out of range 
print(list[2])

# List are mutable, unlike string  
list[0] = "Nahida"
print(list[0])

# a = "Muzamil"
# a[0] = "N" # Error string does not support item assignment 

# List can be sliced like strings 
print(list[0:4])
print(list[1:6])  