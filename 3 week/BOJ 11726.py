import sys

n = int(sys.stdin.readline())

total = []

for i in range(n + 1):
    if i == 0:
        total.append(i)
    
    elif i == 1:
        total.append(i)
    
    elif i == 2:
        total.append(i)
        
    else:
        total.append(total[i - 2] + total[i - 1])
    
print(max(total) % 10007)