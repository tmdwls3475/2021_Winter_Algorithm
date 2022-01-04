import sys

N = int(sys.stdin.readline())
total = []
white = 0
blue = 0

for _ in range(N):
    total.append(list(map(int, sys.stdin.readline().split())))

def color_paper(N, x, y):
    global total, white, blue
    check = 0
    
    for i in range(N):
        for j in range(N):
            check += total[x + i][y + j]
            
    if check == N ** 2:
        blue += 1

    elif check == 0:
        white += 1
    
    else:
        if N == 1:
            return
        for i in range(0, N, N // 2):
            for j in range(0, N, N // 2):
                if not (check == N ** 2) or not (check == 0):
                    color_paper(N // 2, x + i, y + j)
            
color_paper(N, 0, 0)
print(white)
print(blue)