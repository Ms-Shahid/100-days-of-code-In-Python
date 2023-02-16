# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true_list = ['T', 'R', 'U', 'E']
love_list = ['L', 'O', 'V', 'E']

name1 = name1.upper()
name2 = name2.upper()

true_value = 0
for i in true_list:
  true_value += name1.count(i) + name2.count(i)
  print(f"{i} occurs {true_value} times")
print("------------------------")

love_value = 0
for j in love_list:
  love_value += name1.count(j) + name2.count(j)
  print(f"{j} occurs {love_value} times")

total = int(str(true_value) + str(love_value))

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total < 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")
