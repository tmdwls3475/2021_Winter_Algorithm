import sys
from collections import deque

dq = deque()
total = []
N, K = map(int, sys.stdin.readline().split())
count = 0
s = ''

for i in range(1, N + 1):
    dq.append(i)
    
while dq:
    count += 1
    
    if count == K:
        total.append(dq.popleft())
        count = 0
        continue
    
    dq.append(dq.popleft())

for i in range(len(total)):
    if i == 0:
        s += str(total[i])
        continue
    else:
        s += ', ' + str(total[i])
print(f'<{s}>')