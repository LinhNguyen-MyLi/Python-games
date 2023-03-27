# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 11:40:32 2023

@author: Linhnguyen
"""

import random
import datetime

guessesTaken = 0
currentTime = datetime.datetime.now()
currentTime.hour 

if currentTime.hour <12:
    print('Good morning, Hello my dear! What is your name?')
elif currentTime.hour <= currentTime.hour < 18:
    print('Good afternoon, Hello my dear! What is your name?')
else:
    print('Good evening, Hello my dear! What is your name?')


playerName = input()

number = random.randint(1, 10)
print('Nice to meet you, ' + playerName + ' \n'
      'Let play a small game named guessing number, I am thinking of a number between 1 and 10.')
print('\n\tYou have only 5',
      'chances to guess the number!\n')

while guessesTaken <= 5:

    print('Guess what number I am thinking about?') 
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print ('Your guessing number is too low')
    if guess > number:
        print('Your guessing number is too high')
    if guess == number:
        break
    
if guess == number and guessesTaken == 5:
    guessesTaken = str(guessesTaken)
    print('Well done, ' + playerName + 'You got the correct number after ' + guessesTaken + ' guesses!')
if guess == number and guessesTaken == 4:
    guessesTaken = str(guessesTaken)
    print('Nice going, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!', 'Don’t be frustrated my dear, even best friends do not always understand each other')
if guess == number and guessesTaken == 3:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!', 'Practice make perfect')
if guess == number and guessesTaken == 2:
    guessesTaken = str(guessesTaken)
    print('Exellence, ' + playerName + '! You got the correct number after ' + guessesTaken + ' guesses!', 'Keep going! You are on the way becoming mind-reader')
if guess == number and guessesTaken == 1:
    guessesTaken = str(guessesTaken)
    print('Wonderfull, ' + playerName + ' You can call yourself a mind-reader now')
    
if guess != number and guessesTaken > 5:
    number = str(number)
    print('Gameover!!! The correct number is ' + number)