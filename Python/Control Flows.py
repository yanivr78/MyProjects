#!/usr/bin/bash

# Control Flows

print("Welcome to the roller coaster!")

# height = 11 - One equal sign means "Assignment"
# height == 11 - Two Equal signs means "Check Equality"

height = int(input("What is your height in cm?"))
bill = 0

if height > 120:
    print("You can ride the roller-coaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You can enter for free!")
    else:
        bill = 12
        print("Please pay $12")
    wants_photo = input("Do you  want a photo taken ? Y or N")
    if wants_photo == "Y" or "y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("You are too short  to ride the roller coaster")


# Modulo % Gives you the reminder , for example:
# 7 % 2 means How many times does 2 fits in 7 ? - 2 + 2 + 2 + 1 << the remainder is one

# Understanding if a number is odd or even
number = int(input("Which number do you want to check?"))
sum = number % 2
if sum == 1:
    print("This is an odd number.") # Because that dividing it by two will always live 1 as a remainder
elif sum == 0:
    print("This is an even number") # Because that dividing it by 2 will never leave a remainder
else:
    print("Error")