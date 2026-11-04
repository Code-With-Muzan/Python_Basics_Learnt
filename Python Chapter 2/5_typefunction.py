a = "Harry" 
b = type(a) # class <string> , some more examples <float><int><boolean>
print(b)

a = 56783
b = float(a) # convert class <int> into class <float>
c = type(b) # class <int>
print(c)

# Anything enclosed in double qoutes are considered to be a string even if its number too 
a = "3526"
b = type(a)
print(b)