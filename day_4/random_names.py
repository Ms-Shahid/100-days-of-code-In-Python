# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_guess = random.randint(0, len(names)-1)
print(f"{names[names_guess]} is going to buy the meal today!")

#Single line
print(f"{names[random.choice(names)]} is going to buy the meal today!")