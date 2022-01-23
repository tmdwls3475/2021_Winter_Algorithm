import sys
from collections import deque

dq = deque(sys.stdin.readline().rstrip())
dq2 = deque()

s_total = ''
tag_check = False

while len(dq) != 0:
    s = dq.popleft()
    
    if s == '<':
        for _ in range(len(dq2)):
            s_total += dq2.pop()
        s_total += s
        
        tag_check = True
        continue
    
    if s == '>':
        s_total += s
        tag_check = False
        continue
    
    if s == ' ':
        if tag_check:
            s_total += s
            continue
        
        for _ in range(len(dq2)):
            s_total += dq2.pop()
        s_total += s
        continue
        
    if tag_check:
        s_total += s
        continue
    
    else:
        dq2.append(s)
        if len(dq) == 0:
            for _ in range(len(dq2)):
                s_total += dq2.pop()
        continue
print(s_total)