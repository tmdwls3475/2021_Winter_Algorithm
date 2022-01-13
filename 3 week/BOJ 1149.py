import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 1)
Rdp = [0] * (n + 1)
Gdp = [0] * (n + 1)
Bdp = [0] * (n + 1)
R = [0] * (n + 1)
G = [0] * (n + 1)
B = [0] * (n + 1)

for i in range(1, n + 1):
    R[i], G[i], B[i] = map(int, sys.stdin.readline().split())

for i in range(1, n + 1):
    Rdp[i] = min(Gdp[i - 1], Bdp[i - 1]) + R[i]
    Gdp[i] = min(Rdp[i - 1], Bdp[i - 1]) + G[i]
    Bdp[i] = min(Rdp[i - 1], Gdp[i - 1]) + B[i]
    
    dp[i] = min(Rdp[i], Gdp[i], Bdp[i])
    
print(dp[-1])