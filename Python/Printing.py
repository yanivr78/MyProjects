#!/usr/bin/python3
print("Hello World!\n""Hello World!")

# String Concatenation
print("Hello" + " " + "Yaniv")

# Inputs
x = input("What is your name?")
print("This prints the variable x: " + x)

### Shift values
a = input("a: ")
b = input("b: ")

# In here we place a in c, b will overwrite a, and c (which used to be a) will overwrite b
c = a
a = b
b = c

# We will now print the overwritten variables (will appear in reverse order)
print("a: " + a)
print("b: " + b)

# The function input is evaluated first
# Print is evaluated after
print("\nHello " + input("What is your name?") + "!")

#Counts the charachters
print(len(input("What is your name?")))

# Subscripting (Print only a portion of a string)
print("hello"[4])

#F-String
# Since print() doesn't allow to print different datatypes, you can either convert them to be of the same type
# Or use the F-string as so :
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, did you win? {isWinning}")