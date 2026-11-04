# Write a Python program to make a list of six students total marks and sort the alloted marks

marks = []
a = int(input("Enter number one students marks :"))
marks.append(a)
b = int(input("Enter number two students marks :"))
marks.append(b)
c = int(input("Enter number three students marks :"))
marks.append(c)
d = int(input("Enter number four students marks :"))
marks.append(d)
e = int(input("Enter number five students marks :"))
marks.append(e)
f = int(input("Enter number six students marks :"))
marks.append(f)
g = int(input("Enter number seven students marks :"))
marks.append(g)
marks.sort() # If we use sort fuction (String Type) on numbers it will sort in numeric order like one,two,three and so on 
print( "Your Sorted Marks Are :",marks)