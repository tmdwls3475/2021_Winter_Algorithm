import sys

n = int(sys.stdin.readline())
total = []

for i in range(n):
    check = list(map(int, sys.stdin.readline().split()))
    total.append(check)
    
    if i == 0:
        continue
    
    len_check = len(check)
    for j in range(i + 1):
        if j == 0:
            total[i][j] += total[i - 1][j]
            continue
        
        if j == i:
            total[i][-1] += total[i - 1][-1]
            continue
        
        else:
            total[i][j] = max(total[i][j] + total[i - 1][j - 1], total[i][j] + total[i - 1][j])
        
print(max(total[-1]))