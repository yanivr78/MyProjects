#!/usr/bin/python3


# Primitive Data Types
# "12345" - String Data type (You can type in 123_4_5 good for readability) and Python will consider it as 12345).
# 12345 - Integers Data type
# 3.14159 - Float Data type
# True or False - Boolean Data type
#Type() = a function to show you the data type, normally used with print(type(var))

### Converting couple of
num_char = len(input("Whats your name?")) #quantifies that num of characters and store in new_char
new_num_char = str(num_char) #convert the new_char (cause its an int) to a string
print("Your name has " + new_num_char + " characters.") # since new_num_char is a string there will be no errors while trying to print

### converting strings to int
two_digit_number= input("Type two digit number:")

#Get the firest and second digits using subscripting then convert string to int.
result = int(two_digit_number[0]) + int(two_digit_number[1])

print(result)