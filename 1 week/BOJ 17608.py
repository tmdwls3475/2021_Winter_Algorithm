import sys

total = []
count = 0
max = 0

n = int(sys.stdin.readline()) # int(input()) 대신

for _ in range(n):
    total.append(int(sys.stdin.readline().rstrip()))

for _ in range(n):
    total_pop = total.pop(-1)
    if total_pop > max:
        max = total_pop
        count += 1

print(count)