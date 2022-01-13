import sys

n = int(sys.stdin.readline())
floor = [0]
dp = [0] * (n + 1)

for _ in range(n):
    floor.append(int(sys.stdin.readline()))
    
for i in range(1, n + 1):
    if i == 1:
        dp[i] = floor[i]
        continue
    
    if i == 2:
        dp[i] = floor[i] + floor[i - 1]
        continue
    
    dp[i] = max(floor[i - 1] + dp[i - 3], dp[i - 2]) + floor[i]
    
print(dp[-1])