# Write a python program to fill the given template using string functions 
# letter = '''Dear <|Name|>
# You Are Selected 
# <|Date|>'''

a = input("Enter Your Name :")
b = input("Enter Date :")
letter = '''Dear <|Name|>
You Are Selected 
<|Date|>'''
print(letter.replace("<|Name|>", a).replace("<|Date|>", b))