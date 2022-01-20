import sys
from collections import deque

dq = deque()
count = 0
n = int(sys.stdin.readline())

for _ in range(n):
    N = int(sys.stdin.readline())
    
    if N == 0:
        dq.pop()
        continue
    dq.append(N)
    
for i in dq:
    count += i
print(count)