import sys

n = int(sys.stdin.readline())

total = [1, 3]

for i in range(2, n + 1):
    total.append(2 * (total[i - 2]) + total[i - 1])
    
print(total[n - 1] % 10007)