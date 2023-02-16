# tip = 12 / 100
# final_tip = 150 * tip
# total_bill = 150 + final_tip
# total_bill /= 5
# print(total_bill)

print("Welcome to the tip calculator \n -------------------------------")
total_bill = float(input("What was the total bill? $"))
per_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_bill = int(input("How many people to split the bill? "))

final_tip = round(per_tip / 100 * total_bill, 2)
total_bill += final_tip 
total_bill /= split_bill
total_bill = "{:.2f}".format(split_bill)

print(f"Each person should pay: ${total_bill}")