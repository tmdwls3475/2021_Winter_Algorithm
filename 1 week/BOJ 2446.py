n = int(input())
count = 0

for i in range(2 * n - 1, 0, -1):
    if i % 2 == 1:
        print(count * ' ', end = '')
        print('*' * i)
        count += 1

count -= 1

for i in range(2, 2 * n + 1, 1):
    if i % 2 == 1:
        count -= 1
        print(count * ' ', end = '')
        print('*' * i)