n = int(input())

for i in range(n, 0, -1):
    count = int(2 * i - 3)
    
    print(' ' * int(n - i), end = '') # 첫 띄어쓰기
    
    if i == n:
        print('*' * n, end = '')
        print(' ' * count, end = '')
        print('*' * n)
        continue
    
    elif i == 1:
        print('*', end = '')
        print(' ' * int(n - 2), end = '')
        print('*', end = '')
        print(' ' * int(n - 2), end = '')
        print('*')
        continue
        
    else:
        print('*', end = '')
        print(' ' * int(n - 2), end = '')
        print('*', end = '')
        print(' ' * count, end = '')
        print('*', end = '')
        print(' ' * int(n - 2), end = '')
        print('*')
        
for i in range(0, n - 1):
    count = int((i + 1) * 2 - 1)
    
    print(' ' * int(n - i - 2), end = '') # 첫 띄어쓰기
    
    if i == n - 2:
        print('*' * n, end = '')
        print(' ' * count, end = '')
        print('*' * n)
        continue
        
    else:
        print('*', end = '')
        print(' ' * int(n - 2), end = '')
        print('*', end = '')
        print(' ' * count, end = '')
        print('*', end = '')
        print(' ' * int(n - 2), end = '')
        print('*')
