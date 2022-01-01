M = int(input())
N = int(input())

n = 1
total = 0
c = 0
check = True

while 1:
    n_squared = n * n
    if n_squared < M:
        n += 1
        continue

    elif n_squared >= M and n_squared <= N:
        n += 1
        total += n_squared
        if check == True:
            c = n_squared
            check = False
    
    else:
        if not total == 0:
            print(total)
            print(c)
            break
        else:
            print(-1)
            break
