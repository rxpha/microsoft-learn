h = '090'
h = int(h)
x = 0
x = h % 10
h = h // 10
x += h % 10
h = h // 10
x += h
print(x)

j = 234
x = 0
x = j % 10
j = j // 10
x += j % 10
j = j // 10
x += j
print(x)