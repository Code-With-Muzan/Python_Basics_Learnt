# Write a Python Program to enter marks given by user and assign a grade according to its marks [Extra - Take input from the user]

marks = int(input("Enter Your Marks To Assign Grade : "))
if(marks<=100 and marks>=90):
    print("Topper A+ Grade")
elif(marks<90 and marks>=80):
    print("Distinction A Grade")
elif(marks<80 and marks>=70):
    print("First Class B+ Grade")
elif(marks<70 and marks>=60):
    print("Second Class B Grade")
elif(marks<60 and marks>=50):
    print("Third Class C Grade")
elif(marks<50 and marks>=40):
    print("Fourth Class D Grade")
else:
    print("Fail, Better Luck Next Exam")

