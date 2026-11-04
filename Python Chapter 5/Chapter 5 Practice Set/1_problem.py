# Write a Phyton program to make a HinEnglish Dictionary with its English Translation by using Dictionary method [Extra - Input from the user]

word =  {
      "Pyaar" : "Love",   # MTA - To add a string in value assigned to a key in Dictionary, make use of Double Quotes ""
      "Amma" : "Mother", 
      "Khaana" : "Food",
      "Kutta" : "Dog",
      "Billi" : "Cat",
    } 

user = input("Enter A HinEnglish Word To Get The Following Meaning : ")
print(word.get(user))
# print(word[user])