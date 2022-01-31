import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().split())
dq = deque(list(map(int, sys.stdin.readline().split())))
bridge = deque([0] * w)
count = 0

while bridge:
    count += 1
    bridge.popleft()
    
    if len(bridge) < w:
        if sum(bridge) + dq[0] <= L:
            bridge.append(dq.popleft())
        else:
            bridge.append(0)
            
    if sum(dq) == 0:
        count += w
        break
print(count)