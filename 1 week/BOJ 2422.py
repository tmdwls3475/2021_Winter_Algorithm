import sys

ice_num, ice_no_mix_num = map(int, sys.stdin.readline().split())
no_mix_list = [[0 for _ in range(201)] for _ in range(201)]
total = 0

for i in range(ice_no_mix_num):
    no_mix_1, no_mix_2 = map(int, sys.stdin.readline().split())
    no_mix_list[no_mix_1][no_mix_2] = 1
    no_mix_list[no_mix_2][no_mix_1] = 1

for i in range(1, ice_num + 1):
    for j in range(i + 1, ice_num + 1):
        if no_mix_list[i][j]:
            continue
        for e in range(j + 1, ice_num + 1):
            if no_mix_list[i][e] or no_mix_list[j][e]:
                continue
            else:    
                total += 1
print(total)