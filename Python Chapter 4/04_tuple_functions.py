# Tuple Function 

tp = ("apple", "bannana","2", "fog", "true", "false", "354.67","fog")
a = tp.count("fog") # This function tells us about the number of times the variable is repeated in the tuple 
                          # If the variable is not present in the tuple, it returns the output as zero 
print(a)

b = tp.index("fog") # This function tells us about the index of the variable in the tuple 
print(b)                # Note - If the following variable is repeated in the tuple, 
                   # then it will say the index of first occurrence of it in the tuple


# Tuple Slicing

tp2 = tp[1:5]
print(tp2) 

# Tuple concatenate

tp = ("apple", "bannana","2", "fog", "true", "false", "354.67","fog")
tp3 = ("Muzamil","Muzzu")
tp4 = tp + tp3
print(tp4)

# Variable finding in tuple using 'in' function

print("apple" in tp)
print("Muzamil" in tp3)
print("muzu" in tp)
print("Muzzu" in tp4)

# Min and max in tuple 

tp5 = (657,477487,879,84,9876789,4987,94876,987)
print(min(tp5))
print(max(tp5))

# Tuples can be unpacked 

tp = ("apple", "bannana","2", "fog", "true", "false", "354.67","fog")
a,b,c,d,e,f,g,h = tp 
print(a,b,c,d,e,f,g,h)

# These following functions are also applicable for List too