import sys

n = int(sys.stdin.readline())

total = [0, 0, 1, 1]

for i in range(4, n + 1):
    check = []
    
    if i % 2 == 0:
        check.append(total[i // 2] + 1)
        
    if i % 3 == 0:
        check.append(total[i // 3] + 1)
    
    check.append(total[i - 1] + 1)

    total.append(min(check))
print(total[n])