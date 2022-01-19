import sys

n = int(sys.stdin.readline())
result = ''

for _ in range(n):
    
    N = int(sys.stdin.readline())
    sticker_r1_dp = [0] * (N + 1)
    sticker_r2_dp = [0] * (N + 1)
    
    dp = [0] * (N + 1)
    
    sticker_r1 = [0] + list(map(int, sys.stdin.readline().split())) + [0]
    sticker_r2 = [0] + list(map(int, sys.stdin.readline().split())) + [0]
    
    for i in range(1, N + 1):
        if i == 1:
            sticker_r1_dp[i] = sticker_r1[i]
            sticker_r2_dp[i] = sticker_r2[i]
            dp[i] = max(sticker_r1[i], sticker_r2[i])
            continue
        
        sticker_r1_dp[i] = max(sticker_r2_dp[i - 1] + sticker_r1[i], sticker_r2_dp[i - 2] + sticker_r1[i])
        sticker_r2_dp[i] = max(sticker_r1_dp[i - 1] + sticker_r2[i], sticker_r1_dp[i - 2] + sticker_r2[i])
        
        dp[i] = max(sticker_r1_dp[i], sticker_r2_dp[i])
        
    result += str(max(dp)) + '\n'
print(result, end = '')