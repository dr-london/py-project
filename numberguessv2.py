# Guess the number game

import random
import os
import sys

guess = 0
count = 0
number = random.randint(1, 10)

while guess != number and guess != 'exit':
    guess = input('Guess a number between 1 and 10: (or type Exit to quit) ')
    if guess == 'exit':
        break

    guess = int(guess)
    count += 1

    if guess > number:
        print('Too high!')
    elif guess < number:
        print('Too low!')
    else:
        print ('That\'s the correct number, and it took you ' + str(count) + ' tries!')
    
