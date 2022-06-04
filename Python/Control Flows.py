#!/usr/bin/bash

# Control Flows

print("Welcome to the roller coaster!")

# height = 11 - One equal sign means "Assignment"
# height == 11 - Two Equal signs means "Check Equality"

height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the roller-coaster")
else:
    print("You are too short  to ride the roller coaster")