import sys

n = int(sys.stdin.readline())
total = [[' '] * (4 * n - 3) for _ in range((4 * n - 3))]

def star(n, x, y):
    global total
    n1 = (4 * n - 3) # 2 > 5, 3 > 9
    n2 = (4 * n - 5) # 2 > 3, 3 > 7
    
    if n == 1:
        total[x][y] = '*'
        return
    
    for i in range(n1):
        total[x][y + i] = '*'
        total[x + n1 - 1][y + i] = '*'
        
    for j in range(1, n2 + 1):
        total[x + j][y] = '*'
        total[x + j][y + n1 - 1] = '*'
        
    if total[x + 2][y + 2] == ' ':
        star(n - 1, x + 2, y + 2)
        
star(n, 0, 0)
for i in range(len(total)):
    print(''.join(total[i]))