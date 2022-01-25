import sys
from collections import deque

dq = deque()
n = int(sys.stdin.readline())
for i in range(1, n + 1):
    dq.append(i)

dq_num = deque(list(map(int, sys.stdin.readline().split())))
s = ''

while len(dq) != 0:
    balloon = dq.popleft()
    s += str(balloon) + ' '
    balloon_num = dq_num.popleft()
    
    if len(dq) == 0:
        break
    
    if balloon_num > 0:
        for _ in range(balloon_num - 1):
            dq.append(dq.popleft())
            dq_num.append(dq_num.popleft())
    else:
        for _ in range(abs(balloon_num)):
            dq.appendleft(dq.pop())
            dq_num.appendleft(dq_num.pop())

print(s)