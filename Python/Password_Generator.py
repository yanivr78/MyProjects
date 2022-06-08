#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# password = ""


# for num in range(1, nr_letters + 1):
#   # Randomize a letter from nr_letters
#   rand_index_letter = random.randint(0, len(letters) - 1)
#   password += letters[rand_index_letter]

# for num in range(0, nr_numbers + 1):
#   rand_index_num = random.randint(0, len(numbers) - 1)
#   password += numbers[rand_index_num]

# for num in range(0, nr_symbols + 1):
#   rand_index_symbol = random.randint(0, len(symbols) - 1)
#   password += symbols[rand_index_symbol]

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
password = ""

for char in range(1, nr_letters + 1):
  # Randomize a letter from nr_letters
  rand_index_letter = random.randint(0, len(letters) - 1)
  password_list += letters[rand_index_letter]
  # password_list.append(letters[rand_index_letter])

for char in range(0, nr_numbers + 1):
  rand_index_num = random.randint(0, len(numbers) - 1)
  password_list += numbers[rand_index_num]
  # password_list.append(numbers[rand_index_num])

for char in range(0, nr_symbols + 1):
  rand_index_symbol = random.randint(0, len(symbols) - 1)
  password_list += symbols[rand_index_symbol]
  #password_list.append(symbols[rand_index_symbol])

print(f"\nBefore shuffule:\n\n {password_list}\n")
random.shuffle(password_list)
print(f"\nAfter shuffle:\n\n {password_list}\n")

# Converting a list to a string
for char in password_list:
  password += char

print(password)
