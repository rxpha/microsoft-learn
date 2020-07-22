import random, time

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

    count = 0
    roll = 0
    while roll != 5:
        count = count + 1
        roll = random.randint(1, 5)
        # print(f'{name} rolled {roll}')
    else:
        score.append(count)
        print(f'{players[i]} scored {count}!')
time.sleep(1)
print(f'Won who scored ' + str(min(score)) + ' rolls!')
