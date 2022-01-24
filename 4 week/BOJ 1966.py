import sys
from collections import deque

n = int(sys.stdin.readline())
s = ''

for _ in range(n):
    N, M = map(int, sys.stdin.readline().split())
    check = deque([False] * N)
    check[M] = True
    count = 0
    
    dq = deque(list(map(int, sys.stdin.readline().split())))
    
    while len(dq) != 0:
        i = dq.popleft()
        check2 = False
        for j in range(len(dq)):
            if i < dq[j]:
                dq.append(i)
                check.append(check.popleft())
                check2 = True
                break
        if check2:
            continue
        check3 = check.popleft()
        count += 1
        
        if check3:
            s += str(count) + '\n'
print(s, end = '')