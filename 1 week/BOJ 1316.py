N = int(input())
word_list = []
total = 0

for _ in range(N):
    word = input()
    if word not in word_list:
        word_list.append(word)
    
for i in word_list:
    word_check = []
    c = True
    
    for j in range(len(i) - 1):
        if i[j] == i[j + 1]: # 0, 1, 2, 3 / 1, 2, 3, 4
            if i[j] not in word_check:
                word_check.append(i[j])
            continue
        
        else:
            if i[j] not in word_check:
                word_check.append(i[j])
            word_check.append(i[j + 1])
    
    for _ in range(len(word_check)):
        check = word_check.pop(0)
        if check not in word_check:
            continue
        else:
            c = False
            break
    
    if c == True:
        total += 1
print(total)