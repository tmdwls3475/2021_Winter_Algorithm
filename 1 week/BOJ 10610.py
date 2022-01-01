total_list = []
total = 0

n = input()
for i in n:
    total += int(i)
    total_list.append(i)
    
total_list = sorted(total_list, reverse = True)

if total % 3 != 0 or total_list[-1] != '0':
    print(-1)
    
else:
    print(''.join(total_list))