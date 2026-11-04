a = int(input("Enter a Number : "))

for i in range(2,a):
    if (a%i) == 0 :
     print("The number is not a prime")
     break
else:
 print("The number is a prime number")


