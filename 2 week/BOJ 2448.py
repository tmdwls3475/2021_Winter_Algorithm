import sys

N = int(sys.stdin.readline())
total = [[' '] * (2 * N - 1) for _ in range(N)]

def star(N, x, y):
    global total
    
    if N == 1:
        total[x][y] = '*'
    
    else:
        star(N // 2, x, y)
        star(N // 2, x + (N // 2), y - (N // 2))
        star(N // 2, x + (N // 2), y + (N // 2))
        for i in range(-2, 3, 1):
            total[x + 2][y + i] = '*'
        
star(N, 0, N - 1)
for i in total:
    print(''.join(i))