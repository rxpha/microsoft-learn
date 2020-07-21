import random, time

roll = 0
count = 0
qtd = 0
name = ''
players = []
score = []

print('First person to roll a 5 wins!')
qtd = int(input('How many players are going to play? (up to 4)\n'))

for i in range(qtd):
    print('Player #', i+1, ' or \'q\' to quit: ', sep='')
    name = input()
    if name == 'q':
        print('Bye.')
        exit()
    players.append(name)
    while roll != 5:
        count = count + 1
        roll = random.randint(1, 5)
        # print(f'{name} rolled {roll}')
    else:
        score.append(count)
        print(f'{players[i]} scored {count}!')

time.sleep(2)
for k in range(len(score)):
    print(f'{players[k]} won because took less rolls to roll a 5!')
