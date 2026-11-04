a = input("Enter Any Number :")
b = input("Enter Any Number :")
print("Your Entered Number is : ", a)
print("Your Entered Number is : ", b)

# If you try to add up the entered number , then the following numbers will concatenate bcz the entered number is in string type 
a = input("Enter Any Number :")
b = input("Enter Any Number :")
print("Your Entered Number is : ", a)
print("Your Entered Number is : ", b)
print("Sum of the following numbers entered :", a + b) # Example - Number 1 - 546
                                                                #  Number 2 - 987
                                                                #  Output - 5469

# To avoid this error string is coverted into int type using int function
a = int(input("Enter Any Number :"))
b = int(input("Enter Any Number :"))
print("Your Entered Number is : ", a)
print("Your Entered Number is : ", b)
print("Sum of the following numbers entered :", a + b)  # Example - Number 1 - 546
                                                                #  Number 2 - 987
                                                            #  Output - 1533      

                                                        