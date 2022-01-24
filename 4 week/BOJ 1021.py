import sys
import copy
from collections import deque

N, M = map(int, sys.stdin.readline().split())
total = list(map(int, sys.stdin.readline().split()))
count_min = 0

dq = deque()
for i in range(1, N + 1):
    dq.append(i)

for i in total:
    dq2 = copy.deepcopy(dq)
    dq3 = copy.deepcopy(dq)
    check2 = True
    check3 = True
    calc_2 = 0
    calc_3 = 0
    
    while check2:
        s2 = dq2.popleft()
        if s2 == i:
            check2 = False
            continue
        dq2.append(s2)
        calc_2 += 1
        
    while check3:
        s3 = dq3.popleft()
        if s3 == i:
            check3 = False
            continue
        dq3.appendleft(s3)
        dq3.appendleft(dq3.pop())
        calc_3 += 1
    
    if calc_2 >= calc_3:
        count_min += calc_3
        dq = copy.deepcopy(dq3)
    else:
        count_min += calc_2
        dq = copy.deepcopy(dq2)
    
print(count_min)