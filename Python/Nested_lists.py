#/usr/bin/python3

fruits = ["Streberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatos", "Celery", "Potatoes"]
dirty_dosen = [fruits, vegetables]
print(dirty_dosen)
print(dirty_dosen[1][1])
print(dirty_dosen[0][1])

# Nested List Game


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? (write two numbers for the positioning)")

# set first user input
horizontal = int(position[0])
vertical = int(position[1])

# Map is a two-dimensional list , we need to deduct by one (to count from 0) to first
# Locate the Vertical list, and then the Horizontal cell number.

# This will replace the Cell with the letter "X"
selected_row = map[vertical -1]
map[vertical - 1][horizontal - 1] = "X"

# Printing the new rows
print(f"{row1}\n{row2}\n{row3}")