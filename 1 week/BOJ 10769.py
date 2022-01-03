import sys

happy = 0
sad = 0

s = sys.stdin.readline()
for i in range(len(s)):
    if s[i] == ':':
        if s[i + 1] == '-':
            if s[i + 2] == ')':
                happy += 1
            if s[i + 2] == '(':
                sad += 1

if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')