import sys
from collections import deque

dq = deque()
n = int(sys.stdin.readline())
i = 1
s = ''
check2 = 0

for _ in range(n):
    check = False
    N = int(sys.stdin.readline())
    
    while i <= N:
        dq.append(i)
        i += 1
        s += '+' + '\n'
        
    t = dq.pop()
    
    if t == N:
        s += '-' + '\n'
        check = True
        
    if not check:
        check2 += 1

if not check2:
    print(s, end = '')
else:
    print('NO')