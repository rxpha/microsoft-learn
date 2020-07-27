import random
import time

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for suit in suits: 
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

print(f'There are ' + str(len(deck)) + ' cards in the deck.')
time.sleep(0.8)
print('Dealing', end='')
for i in range(3):
    time.sleep(0.3)
    print('.', end='')

player = []
player.append(random.choices(deck,k=5))
print(f'\nThere are ' + str(len(deck)-5) + ' cards in the deck.')
print(f'Player has the following cards in his hand:')
print(player)

import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for  suit in suits:
  for rank in ranks:
    deck.append(f'{rank} of {suit}')

print(f'There are {len(deck)} cards in the deck.')

print('Dealing ...')

hand = []

while len(hand) < 5:
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

print(f'There are {len(deck)} cards in the deck.')
print('Player has the following cards in their hand:')
print(hand)