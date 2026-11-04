import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Hello everyone . Today i am going to speak this text")
engine.runAndWait()

# So this is a program which i copied from a site called pyttsx3
# First - u got to import pyttsx3 from the official website 
# Second - then u have to scrool a bit on the website to find the usage section and copy it once you find it entirely
# Then paste on Visual code editor and edit uour text in engine.say commmand section
# That's all run your program and enjoy the speech being said 