# If statement

a = 19
if(a>=18):
    print("Good")
#-> Space btw is called as Indent

# If Else Statement/Ladder

b = 20
if(b>=18):
    print("Good")
else :
    print("Bad")

# If Elif Else Statement/Ladder 

c = 0
if(c>=18):
    print("Good")
elif(c==0):
    print("Invalid Number")
else :
    print("Bad")

# Nested If Else Statement 

d = 11
if(d>10):
    print("Good")
    if(d>=18):
        print("Just Good")
    else:
        print("But Less Than 18")
else:
    print("Bad")