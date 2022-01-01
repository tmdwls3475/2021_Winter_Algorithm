n = int(input())
n_list = [999] * n

order = input().split()

for i in range(n):
    count = 0
    for j in range(n):
        if count == int(order[i]):
            if n_list[j] != 999:
                continue
            n_list[j] = i + 1
            break
        
        if n_list[j] > i + 1:
            count += 1
        
for _ in range(len(n_list)):
    print(n_list.pop(0), end = ' ')
