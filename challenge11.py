import random
x = random.randint(1, 10)
count = 0
n = 0
print('Guess a number between 1 and 10')
while n != x:
    count += 1
    n = input(f'Enter guess #{count}: ')
    if n.isnumeric():
        n = int(n)
        if n < x:
            print('Your guess is too low, try again!')
        if n > x:
            print('Your guess is too high, try again!')
    else:
        print('Numbers only, please!')
else:
    print(f'You guessed it in {count} tries!')