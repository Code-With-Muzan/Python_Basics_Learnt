# Write a Python program to check whether the given Instagram message is talking about that specific person name are not [Extra - Take input from the user]

message = input("Enter Your Instagram Message : ")
if("Muzamil".lower() in message.lower()):
    print("Yes, he/she is talking about Muzamil aka The Editor")
else:
    print("Its not that person he/she is talking about")