# String Slicing

name = 'Muzamil'
    #  -> length = 6
    #   0123456 - Numbering in programming, index always starts from zero 
    #  -6-5-4-3-2-1 - Numbering from the end of the given string 
a = len(name)
b = name[6] # Prints character l from the string
print(a)
print(b)

name = "Muzamil"
c = name[0:5] # starts from 0 and end it till 5 but excludes the charcter in position 5 like i in the string 
d = name[0:3] # starts from 0 and end it till 3 but excludes the charcter in position 3 like a in the string
print(c)
print(d)