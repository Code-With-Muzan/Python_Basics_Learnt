#  Use the In - Built Module to print directory path contents of your system using os module 

import os
directorypath = '/'
contents = os.listdir(directorypath)
print(contents)