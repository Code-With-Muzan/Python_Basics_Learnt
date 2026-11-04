# Write a Python program to make a list of seven fruits entered by the user 

a = input("Enter number one fruit :")
b = input("Enter number two fruit :")
c = input("Enter number three fruit :")
d = input("Enter number four fruit :")
e = input("Enter number five fruit :")
f = input("Enter number six fruit :")
g = input("Enter number seven fruit :")
fruits = [a,b,c,d,e,f,g]
print("Your Following Fruits Are =", fruits)

# Another method using list function - append function 

fruits = []
a = input("Enter number one fruit :")
fruits.append(a)
b = input("Enter number two fruit :")
fruits.append(b)
c = input("Enter number three fruit :")
fruits.append(c)
d = input("Enter number four fruit :")
fruits.append(d)
e = input("Enter number five fruit :")
fruits.append(e)
f = input("Enter number six fruit :")
fruits.append(f)
g = input("Enter number seven fruit :")
fruits.append(g)
print(fruits)