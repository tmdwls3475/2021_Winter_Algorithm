n = int(input())
sentence_list = []

for _ in range(n):
    sentence = input().split(' ')
    sentence_basic = ''
    for i in range(len(sentence)):
        if len(sentence[i]) == 1:
            sentence_basic += sentence[i] + ' '
        else:
            sentence_basic += ''.join(reversed(sentence[i])) + ' '
    sentence_list.append(sentence_basic)
    
for i in range(n):
    print(sentence_list[i])
