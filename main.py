# make list of actions

import random

while True:

choices = ['Rock', 'Paper', 'Scissors']

computerAction = random.choice(choices).lower()

playerAction = input('Rock, Paper, or Scissors?').lower()

print(f'Player chose: {playerAction}')
print(f'Player chose: {computerAction}')

if playerAction == computerAction:
    print('Tie!')

elif playerAction == 'rock' and computerAction == 'paper':
    print('Computer wins!')
elif playerAction == 'rock' and computerAction == 'scissors':
    print('Player wins!')

elif playerAction == 'paper' and computerAction == 'scissors':
    print('Computer wins!')
elif playerAction == 'paper' and computerAction == 'rock':
    print('Player wins!')

elif playerAction == 'scissors' and computerAction == 'rock':
    print('Computer wins!')
elif playerAction == 'scissors' and computerAction == 'paper':
    print('Player wins!')