import sys

n = int(sys.stdin.readline())
check = []

total = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    count = 1
    for j in range(i):
        if total[i] > total[j]:
            count = max(count, check[j] + 1)
        
    check.append(count)
print(max(check))