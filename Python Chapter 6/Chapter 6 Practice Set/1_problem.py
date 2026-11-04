# Write a Python program to compare four numbers entered by the user and tell which one is the largest [Extra - Take input from the user]

a = int(input("Enter Your First Number : "))
b = int(input("Enter Your Second Number : "))
c = int(input("Enter Your Third Number : "))
d = int(input("Enter Your Fourth Number : "))

if(a>b and a>c and a>d):
    print("A Is The Largest : ",a)
elif(b>a and b>c and b>d):
    print("B Is The Largest : ",b)
elif(c>b and c>a and c>d):
    print("C Is The Largest : ",c)
else:
    print("D Is The Largest : ",d)