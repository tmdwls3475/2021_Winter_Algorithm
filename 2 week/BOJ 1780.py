import sys

N = int(sys.stdin.readline())
total = []
zero = 0
one = 0
minus_one = 0
total_str = ''

for _ in range(N):
    total.append(list(map(int, sys.stdin.readline().split())))
    
def paper_num(N, x, y):
    global total, zero, one, minus_one
    check = 0
    
    for i in range(N):
        for j in range(N):
            if total[x][y] != total[x + i][y + j]:   
                for i in range(0, N, N // 3):
                    for j in range(0, N, N // 3):
                        paper_num(N // 3, x + i, y + j)
                return
            else:
                check += total[x + i][y + j]
            
    if check == 0:
        zero += 1
        return
            
    elif check == N ** 2:
        one += 1
        return

    elif check == -(N ** 2):
        minus_one += 1
        return
    
    else:
        if N == 1:
            return
            
paper_num(N, 0, 0)
print(minus_one)
print(zero)
print(one)