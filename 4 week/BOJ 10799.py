import sys
from collections import deque

dq = deque(sys.stdin.readline())

count = 0
total = 0
check2 = False

while len(dq) != 0:
    check = dq.popleft()
    
    if check == '(':
        count += 1
        check2 = True
        continue
    
    if check == ')':
        count -= 1
        
        if check2 == True:
            check2 = False
            
            if count == 0:
                continue
            else:
                total += count
                
        else:
            total += 1
            continue

print(total)