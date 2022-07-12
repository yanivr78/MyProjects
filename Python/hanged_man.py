#!/usr/bin/python3
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6

#Step 1
word_list = ["chun", "yaniv", "ariela", "nicole"]
import random
chosen_word = random.choice(word_list)


#Testing Code

# Create an empty list so that if the word is babbon, display should be like so:
# ["_", "_", "_", "_", "_", "_"]
display=[]
for letter in chosen_word:
    display += "_"

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  #E.g If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
  for position in range(len(chosen_word)):
  # In here we overwrite the offset in each iteration (e.g. if its apple then : a,p,p,l,e) and assign it to 'letter'
    letter = chosen_word[position]
    if letter == guess:
  # We overwrite the "_" with the letter
      display[position] = letter
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      print("You lose.")
      end_of_game = True


  print(f"{' '.join(display)}")

  if "_" not in display:
    print("You win!")
    end_of_game = True

  print(stages[lives])