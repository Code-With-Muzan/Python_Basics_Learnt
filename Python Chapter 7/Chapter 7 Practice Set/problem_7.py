# n = 4
#    *
#   ***
#  *****
# *******

n = int(input("Enter a Number : "))
for i in range(1,n+1):
    print(" " * (n-i), end = "")
    print("*" * (i))
print("End of Program")

# n = 3
# *****
#  ***
#   *

# n = int(input("Enter a Number : "))
# for i in range(1,n+1):
#     print(" " * (i - 1), end ="")
#     print("*" * (2 * (n - i) + 1))
# print("\n")
# print("End Of Program")