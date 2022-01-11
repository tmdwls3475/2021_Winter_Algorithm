import sys

def plus(N):
    
    if N > 3:
        return plus(N - 1) + plus(N - 2) + plus(N - 3)
    
    if N == 3:
        return total[N - 1]
    
    if N == 2:
        return total[N - 1]
    
    if N == 1:
        return total[N - 1]

n = int(sys.stdin.readline())
str = ''

for _ in range(n):
    total = [1, 2, 4] # 1, 2, 3 일 때
    N = int(sys.stdin.readline())
    
    count = plus(N)
    str += f'{count}\n'

print(str, end = '')