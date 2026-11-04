marks =  {                
         "Muzamil" : 100,
         "Muzzu" : 23,      
         "Muz" : 45,
         "MUzzzuu" : 46
       }

# Dictionaries Methods 

print(marks.items()) # This functions gives us the list of key value pair tuple 
print(marks.keys()) # This function gives us the list of keys
print(marks.values()) # This function gives us the list of values 
print(marks.get("Muzamil")) # This funarch the key and retuns the assigned value to it, if not found retuns none 
marks.update({ "Nahida" : 100}) # This function updates the values of keys and it also add a new (key,value) pair 
print(marks)

# Difference btw get and marks[] fuction 

print(marks.get("Muzail")) # If this function does not find the key, it will return the output none 
print(marks["Muzail"]) # But this function will return an error if it does not find the key entered 

# Extra Dictionaries methods

marks.clear() # This function will remove all key value pairs and will return an empty dictionary
print(marks)
marks.copy() # This function will return a copy of the dictionary 
print(marks)
marks.popitem() # This function will pop a random (key,value) pair 
print(marks)
marks.pop("Muzamil") # This function will remove a entered (key,value) pair from the dictionary
print(marks)
print(len(marks)) # This function tells the length of the dictionary