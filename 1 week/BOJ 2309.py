import sys

total = []
total_sum = 0
check = False
p = ''

for _ in range(9):
    n = int(sys.stdin.readline().rstrip())
    total.append(n)
    total_sum += n
    
for i in range(8):
    for j in range(i + 1, 9):
        if (total[i] + total[j]) == (total_sum - 100):
            a = total[i]
            b = total[j]
            total.remove(a)
            total.remove(b)
            check = True
            break
    if check == True:
        break

total.sort()

for i in total:
    p += (str(i) + '\n')
print(p)