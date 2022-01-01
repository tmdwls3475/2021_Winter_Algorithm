N = int(input())
arr = [['*'] * N for _ in range(N)]

def star(N, x, y):
    global arr
    
    for i in range(N // 3, (N // 3) * 2):
        for j in range(N // 3, (N // 3) * 2):
            arr[x + i][y + j] = ' '
    
    if N == 1:
        return
    
    for i in range(0, N, N // 3):
        for j in range(0, N, N // 3):
            star(N // 3, x + i, y + j)
        
star(N, 0, 0)
for i in arr:
    print(''.join(i))