N = int(input())
count = 0

while N > 0:
    if N // 5 and N % 5 == 0: # 5로만 될 때
        N -= 5
        count += 1

    elif N // 3 and N % 3 == 0: # 3으로만 될 때
        N -= 3
        count += 1
        
    elif (N % 5) % 3 == 0 or (N % 3) % 5 == 0: # 3과 5로 될 때
        N -= 5
        count += 1
        
    elif not ((N // 5) // 3 == 0 or (N // 3) // 5 == 0): # 3과 5로 될 때
        N -= 5
        count += 1

    else:
        for _ in range(N // 5 - 1):
            if (N - 5) % 3 == 0:
                N -= 5
                count += 1
                
            else:
                N -= 5
                count += 1

        if not N % 3 == 0 or N % 5 == 0:
            print(-1)
            break

if count:
    print(count)
