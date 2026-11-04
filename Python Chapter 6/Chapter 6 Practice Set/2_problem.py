# Write a Python program to check whether the given student marks is above 33 in all subjects and total percentage is above 44, if not fail [Extra - Take input from the user]

a = int(input("Enter Your First Marks : "))
b = int(input("Enter Your Second Marks : "))
c = int(input("Enter Your Third Marks : "))
d = int(input("Enter Your Fourth Marks : "))

if(a<=100):
    if(b<=100):
        if(c<=100):
            if(d<=100):
                tp = ((a + b + c + d)/400)*100
            else : 
                print("Invalid Marks")
        else:
            print("Inavalid Marks")
    else:
        print("Invalid Marks")
else:
    print("Invalid Marks")

if(tp>=44 and a>33 and b>33 and c>33 and d>33):
    print("You Have Passed,","Congratulations !".upper())
    print("Your Total Percentage : ",tp)
else:
    print("You Have Failed, Better Luck Next Year !")
    print("Your Total Percentage : ",tp)

