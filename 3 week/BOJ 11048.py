import sys

N, M = map(int, sys.stdin.readline().split())
room = [0]

for _ in range(N):
    room.append([0] + list(map(int, sys.stdin.readline().split())))
    
dp = [[0] * (M + 1) for _ in range(N + 1)]
    
for i in range(1, N + 1):
    for j in range(1, M + 1):
        
        if i == 1 and j == 1:
            dp[i][j] = room[i][j]
            continue
        
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + room[i][j]
        
print(dp[N][M])