# Rock paper scissors v2
import random
import sys

rps = ['rock', 'paper', 'scissors']
p1 = input('Rock, paper or scissors? ')
p1 = p1.lower()
print('You\'ve chosen: ' + p1.title())
p1 = str(p1)
val = random.randint(0,2)
p2 = rps[val]
print('Computer chooses: ' + p2.title())

if p1 not in rps:
        print('Please input rock, paper, or scissors and try again.')
        sys.exit()

def compare(u1, u2):
    while True:
        if u1 == 'rock':
            if u2 == 'scissors':
                return('You win')
        elif u1 == 'paper':
            if u2 == 'rock':
                return('You win')
        elif u1 == 'scissors':
            if u2 == 'paper':
                return('You win')
        elif u1 == u2:
            return('Draw.')
        else:
            return('You lose.')

print(compare(p1, p2))

while True:
    quit = input('Do you want to play again? (Yes/No) ')
    if quit.title() == 'No':
        break
        




   
    
