list = ["apple", "bannnana", "2", "fog", "true", "false", "354.67"]

list.append("Muzamil")
print(list)

list.extend('Muzamil') # Unlike like append, this appends each element of a given string
print(list)

list.sort()
print(list)

list.reverse()
print(list)

list.insert(4,"Muzzu")
print(list)

a = list.pop() # This functions removes the varible from the list at the inputted index of the list
print(a)

list.remove("2") # Unlike like pop, we have to input the variable from the list in order to remove it from the list 
print(list)   
