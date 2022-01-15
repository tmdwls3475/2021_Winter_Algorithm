import sys

n = int(sys.stdin.readline())
total = [[' '] * (((2 ** n) - 1) * 2 - 1) for _ in range((2 ** n) - 1)]

def star(n, x, y):
    global total
    n1 = (2 ** n) - 1
    n2 = n1 * 2 - 1
    
    if n == 1:
        total[x][y] = '*'
        return
    
    if n % 2 == 0:
        for i in range(n2):
            total[x][y + i] = '*'
        
        for i in range(1, n1):
            if i == n1 // 2:
                star(n - 1, x + i, y + 1 + i)
            total[x + i][y + i] = '*'
            total[x + i][y + n2 - 1 - i] = '*'
            
    if n % 2 == 1:
        for i in range(n2):
            total[x][y + i] = '*'
            
        for i in range(1, n1):
            if i == n1 // 2:
                star(n - 1, x - i, y + 1 + i)
            total[x - i][y + i] = '*'
            total[x - i][y + n2 - 1 - i] = '*'

if n % 2 == 0:
    star(n, 0, 0)
    
    for i in range(len(total)):
        for j in range((((2 ** n) - 1) * 2 - 1) - i):
            print(total[i][j], end = '')
        print()
else:
    star(n, (2 ** n) - 2 , 0)
    
    for i in range(len(total)):
        for j in range((2 ** n) - 1 + i):
            print(total[i][j], end = '')
        print()

# if n % 2 == 0:
#     star(n, 0, 0)
    
# else:
#     star(n, (2 ** n) - 2 , 0)

# for i in range(len(total)):
#     print(''.join(total[i]))