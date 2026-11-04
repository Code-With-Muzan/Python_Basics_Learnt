# What will be the length of the following set ?

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))

# The length of the following set will be 2 
# Bcz in Phyton if both the numbers are numerically (i.e - 20 == 20.0) equal ignoring the type of data entered (i.e - Integer and Float),
                     # then it will return the output as true and for this problem as an unique value 