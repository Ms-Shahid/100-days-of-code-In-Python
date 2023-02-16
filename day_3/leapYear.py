
year = int(input("Which year do you want to check? "))

#Refer good-notes for flow chart
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
          print("leap year.")
    else:
      print("leap year.")
else:
    print("Not leap year.")
