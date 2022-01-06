import sys

n = int(sys.stdin.readline())
count = 0
total = []

for i in range(n + 1):
    if i == 0:
        total.append(i)
    elif i == 1:
        total.append(i)
    else:
        count = total[i - 1] + total[i - 2]
        total.append(count)
        
print(f'{total[n]}')