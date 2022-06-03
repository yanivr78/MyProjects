#!/usr/bin/python3

# Tip Calculator 
# If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?"))
tip = int(input("What precantage tip would you like to give?"))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
# Turns the float final_amount into a string to fix the presentation and show final_amount.00 (two decibals)
final_amount = "{:.2f}".format(bill_per_person) 
print(f"The tip amount is {total_tip_amount} The Total amount with tip is : {total_bill} Each person should pay ${final_amount}")
