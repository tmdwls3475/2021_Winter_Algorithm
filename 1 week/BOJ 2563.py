n = int(input())
l = [[0] * 100 for _ in range(100)]
rect = []
count = 0

for _ in range(n):
    weight, height = map(int, input().split())
    for i in range(10):
        for j in range(10):
            l[height + i][weight + j] = 1
            
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][j] == 1:
            count += 1

print(count)