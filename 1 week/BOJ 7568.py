import sys

n = int(sys.stdin.readline())
total = []
rank_list = []

for _ in range(n):
    detail = tuple(map(int, sys.stdin.readline().split()))
    total.append(detail)

for i in range(n):
    rank = 1
    for j in range(n):
        if total[i][0] < total[j][0] and total[i][1] < total[j][1]:
            rank += 1
    print(rank, end = ' ')