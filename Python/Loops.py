#!/usr/bin/python3

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)

# Calculate average
# Enter student heights with space as a delimiter
# Example : 180 124 165 173 189 169 146 would result in an avg of 164
students_heights = input("Input a list of student heights").split()
total = 0

for n in range(0, len(students_heights)):
    total += int(students_heights[n])  # This is what sum() function do


num_of_students = 0
for student in students_heights:
    num_of_students += 1 # This is what len() function do

avg = round(total / num_of_students)
print(avg)

# You can use min() or max() which will perform something like this :
# This is an example for max():

# count from 1 to 9 with a step of 2
for i in range(1, 10, 2):
    print(i)

# Transform students hight list strings to int
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

highest_num = 0
for high in students_heights:
    if high > highest_num:
        highest_num = high
print(f"This is is the highest height : {highest_num}")
