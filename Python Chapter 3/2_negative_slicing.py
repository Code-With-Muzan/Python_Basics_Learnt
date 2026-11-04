# Negative Slicing

name = "Muzamil"
     #  -6-5-4-3-2-1 - Numbering from the end of the given string (Negative Indices)

a = name[-5:-2] # Starts from -5 and end it till -2 but excludes the charcter in position -2 like m in the string 
b = name[-6:-1] # Starts from -6 and end it till -1 but excludes the charcter in position -1 like l in the string
print(a)
print(b)

print(name[:7]) # Starts from 0 if not written and ends at the mentioned last index 
print(name[0:]) # Starts from the mentioned first index 0 and ends at the end of string if not written 
print(name[:])

# Skip Value 

name_2 = "Muzamil"
print(name_2[0:5:2]) # It starts from zero and ends and excludes 5 , then from start it skips two character in the string and print the character after 2nd charcter - Mzi
print(name_2[0:4:3]) # It starts from zero and ends and excludes 4 , then from start it skips three character in the string and print the character after 3rd charcter - Ma|