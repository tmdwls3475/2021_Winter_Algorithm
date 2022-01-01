ice_n = input().split()
ice_ncombine = []
count = 0

for i in range(int(ice_n[1])):
    n = input().split()
    ice_ncombine.append((int(n[0]), int(n[1])))

for i in range(1, int(ice_n[0])):
    for j in range(i + 1, int(ice_n[0]) + 1):
        if ((i, j) in ice_ncombine) or ((j, i)) in ice_ncombine:
            continue
        count += 1
        
print(count)
