# Rock paper scissors

import random

# Get the input from p1, p2

rps = ['rock', 'paper', 'scissors']
p1 = input('Rock, paper or scissors? ')
p1 = p1.lower()
print('You have selected: ' + p1.title())

#p2 = input('P2: rock, paper or scissors?')
  #print('You have selected: ' + p2)
while True:
    if (p1) not in rps:
        print('Please input rock, paper, or scissors'):
          sys.exit()
# Compare inputs
p1 = str(p1)
val = random.randint(0,2)
p2 = rps[val]
print('Computer has chosen: ' + p2.title())
# Output result
if p1 == 'rock' and p2 == 'scissors':
    print('You win')
elif p1 == 'paper' and p2 == 'rock':
    print('You win')
elif p1 == 'scissors' and p2 == 'paper':
    print('You win')
elif p1 == p2:
    print('Draw!')
else:
    print('You lose')
# Play again condition - break cannot stop if statements
quit = input('Press q to quit')
if quit == 'q':
     break
else 
