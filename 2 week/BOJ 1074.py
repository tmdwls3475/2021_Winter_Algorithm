import sys

N, row, column = map(int, sys.stdin.readline().split())
count = 0

def Z(N, x, y):
    global count, row, column
    #squared2 = 2 ** (N - 1)
        
    if N == 0:
        count += 1
        return
    
    if row < 2 ** (N - 1):
        if column < 2 ** (N - 1):
            row = row % 2 ** (N - 1)
            column = column % 2 ** (N - 1)
            Z(N - 1, x, y)
        else:
            row = row % 2 ** (N - 1)
            column = column % 2 ** (N - 1)
            count += (2 ** (N - 1) * 2 ** (N - 1))
            Z(N - 1, x, y + 2 ** (N - 1))
        
    else:
        if column < 2 ** (N - 1):
            row = row % 2 ** (N - 1)
            column = column % 2 ** (N - 1)
            count += 2 * (2 ** (N - 1) * 2 ** (N - 1))
            Z(N - 1, x + 2 ** (N - 1), y)
        else:
            row = row % 2 ** (N - 1)
            column = column % 2 ** (N - 1)
            count += 3 * (2 ** (N - 1) * 2 ** (N - 1))
            Z(N - 1, x + 2 ** (N - 1), y + 2 ** (N - 1))

Z(N, 0, 0)
print(count - 1)