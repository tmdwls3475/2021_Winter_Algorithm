import sys

N = int(sys.stdin.readline())
total = []
result = []

for _ in range(N):
    str_line = []
    line = sys.stdin.readline().rstrip()
    for i in line:
        str_line.append(int(i))
    total.append(str_line)

def quad_tree(N, x, y):
    global total, result
    one_count = 0
    zero_count = 0
    
    for i in range(N):
        for j in range(N):
            if total[x + i][y + j] == 1:
                one_count += 1
            else:
                zero_count += 1
                
    if N == 1:
        print(total[x][y], end = '')
        return
    
    if not (one_count == N ** 2 or zero_count == N ** 2):
        print('(', end = '')
        for i in range(0, N, N // 2):
            for j in range(0, N, N // 2):
                if quad_tree(N // 2, x + i, y + j):
                    print(quad_tree(N // 2, x + i, y + j), end = '')
        print(')', end = '')
        
    if one_count == N ** 2:
        print(total[x][y], end = '')
        return
        
    if zero_count == N ** 2:
        print(total[x][y], end = '')
        return
    
quad_tree(N, 0, 0)