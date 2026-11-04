# Write a Python program to check the given youtube comment by the user is spam or not [Extra - Take input from the user]

m1 = "Click This"
m2 = "Mr Beast Give Me Money"
m3 = "Make Money"
m4 = "Subscribe Me Please"

message = input("Enter The Message : ")
if(m1.lower() in message.lower()) or (m2.lower() in message.lower()) or (m3.lower() in message.lower()) or (m4.lower() in message.lower()):
    print("This Message Is Spam")
else:
    print("This Message Is Not A Spam") 