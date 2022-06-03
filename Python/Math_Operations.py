#!/usr/bin/python3

# 3 + 5
# 7 - 4
# 3 * 2
# print(6 / 3) # the result will be "2.0" and not "2" - Division always turns into a float datatype
# print(6 // 3) # The result will be an int 2 (and not the float 2.0)
# print(2 ** 3) # 2 by the power of 3 = 8


### Math orders are following PEMDAS from left the right (Parentheses "()", Exponents "**", Multipliction "*" and Divison "/" , Addition "+" and Subtraction "-")

print(3 * (3 + 3) / 3 -3)
# The flow is as so :
# We are starting from the left side and evaluate the equation
# 3 * (6) / 3 - 3
# 18 / 3 - 3
# 6 - 3 = 3.0 # Python always creates a float (3.0 and not 3) for divisions

# calculating into a var
result = 4 / 2 # Four divided by 2
result /= 2 # The characters /= means 2.0 (i.e, result) divided by 2
print(result) # it will show the output : 1.0

# Sometimes a scoreboard on a game will need to use increments like so :
score = 0
score += 1
print(score)

#Round numbers
print(round(8 / 3, 2)) # 8 / 3 and then round to two decimal places (2.67 instead of 2.666666666)
