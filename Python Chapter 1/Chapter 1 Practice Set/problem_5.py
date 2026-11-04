# Label each line of code usinng single line comment 

# Imports the in-built module of python known as os 
import os 

# Specify the directory you want 
directory_path = '/'  

# List all the directories and files in specified path 
contents = os.listdir(directory_path)

# Prints all the contents present in directory path 
print (contents)