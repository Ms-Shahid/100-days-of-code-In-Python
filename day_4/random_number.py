import random

random_int = random.randint(100,200)
random_float = random.random() #returns 0 to < 1
random_float *= 5

print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

random_guess = random.randint(0,1)
if random_guess == 0:
  print('Heads')
else:
  print('Tails')