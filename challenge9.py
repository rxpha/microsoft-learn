# import random as dice
# roll = dice.randint(1, 10)
# print(f'You rolled {roll}.')

# import emoji
# message = emoji.emojize('wtf :sun_with_face:')
# print(message)

import random, emoji

roll = 0
count = 0

while roll != 5:
  count = count + 1
  roll = random.randint(1, 5)
  print(roll)

print(f'It took {count} rolls to roll a 5!')
message = emoji.emojize(f'eu so pika :thumbs_up:')
print(message)

