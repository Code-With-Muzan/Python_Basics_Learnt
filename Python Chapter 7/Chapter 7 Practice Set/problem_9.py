# n = 3

# ***
# * *
# ***
while True:
 
 n = int(input("Enter a Number : "))
 for i in range(1,n+1):
    if(i==1 or i==n):
        print("*" * n )
    else:
        print("*",end="")
        print(" " * (n-2),end="")
        print("*")

 a = input("Do U Want More Stars : Yes/no? - ")
 if(a.lower() == "NO".lower()):
    print("Thank You !\nEnd Of Program")
    break
 elif(a.lower() == "yes".lower()):
    continue
 else:
    print("Invalid Choice")
   