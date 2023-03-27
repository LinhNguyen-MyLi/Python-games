# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:35:04 2023

@author: Linhnguyen
"""

import random

print('Hello my dear! What is your name?')

playerName = input()
print('Nice to meet you, ' + playerName + ' \n'
                                          'My name is Rob, like rob in robot.')

player_play = input('Will you play ROCK PAPER SCISSORS game with me?[yes/no]')
if player_play == "yes":
    print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
          + "Rock vs Paper -> Paper wins \n"
          + "Rock vs Scissors -> Rock wins \n"
          + "Paper vs Scissors -> Scissor wins \n")
elif player_play == "no":
    print("Maybe next time, see you around")
    quit()
else:
    print("Please type yes or no")

arr = ["rock", "scissors", "paper"]

# rob_choice = arr[random.randint(0,2)]

play = True
while play:
    rob_choice = arr[random.randint(0, 2)].lower()
    player_choice = input()
    print("Your choice is " + player_choice + ", my choice is" + rob_choice)

    if player_choice == rob_choice:
        print("Tie")

    elif player_choice == "rock":
       if rob_choice == "paper":
          print("You lose!")
       else:
          print("You win, well done!")

    elif player_choice == "scissors":
       if rob_choice == "rock":
          print("You lose!")
       else:
        print("You win, well done!")

    elif player_choice == "paper":
       if rob_choice == "scissors":
          print("You lose!")
       else:
        print("You win, good job!")
    else:
        print("Oh common, you should type it correctly. Just rock, scissors or paper")

    rob_choice = arr[random.randint(0, 2)].lower()

    play_more = input("Do you want to play again? (yes/no): ")
    if play_more.lower() in ('no', 'n'):
        print('Thank you for the game, see you around!')
        quit()
