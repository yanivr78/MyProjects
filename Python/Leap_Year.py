#!/usr/bin/python3

# This program will check to see if a year is a leap year or not (search google for leap year)
# The 3 conditions that it follows are  (formulated in a nested conditional way):
#
# On every year that is evenly divisible by 4
#   Except every year that is evenly divisible by 100
#       Unless the year is also evenly divisible by 400

year = int(input("Which year do you want to check?"))


if year % 4 == 0 :
    print("Year cleanly divided by 4, continuing second IF")
    if year % 100 == 0:
        print(f"Cleanly divided by 100, continuing to third IF")
        if year % 400 == 0:
            print("Cleanly divided with 400, Leap year")
        else:
            print("Didn't cleanly divided by 400 - Not a leap year")
    else:
        print("Didn't cleanly divided by 100 so its a Leap year.")
else:
    print("Didn't cleanly divided by 4 - Not a leap year")