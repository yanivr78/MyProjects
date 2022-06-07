#!/usr/bin/python3
import random

random_integer = random.randint(1, 10)
random_float = random.random()
print(f"{random_integer}\n{random_float}")

# Head or tails game
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

# Russian roulette of whose going to pay

# Split string method
names_string = input("Give me everybody's names, separated by a comma")
names = names_string.split(",")

# Get the total number of items in list
num_items = len(names)

# since len starts from 1 and we start to count from 0, we will deduct by -1
random_choice = random.randint(0, num_items - 1)
print(f"{names[random_choice]} will pay.")