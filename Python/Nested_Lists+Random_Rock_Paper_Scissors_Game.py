import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Your choice
players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

# A randomized number for the two-dimensional list (computers_response[x])
random_choice = random.randint(0,2)
choices = [rock, paper, scissors]

player_chose = choices[players_choice]
computer_chose = choices[random_choice]

print(f"{player_chose}\n Computer Chose: \n{computer_chose}")

if player_chose == computer_chose:
    print("Its a draw!")

elif (player_chose == choices[0] and computer_chose == choices[2]) or (player_chose == choices[1] and computer_chose == choices[0])  or (player_chose == choices[2] and computer_chose == choices[1]) :
    print("You won!")

else:
    print("You lose!")