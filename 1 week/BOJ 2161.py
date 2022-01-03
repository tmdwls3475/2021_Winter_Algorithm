import sys

n = int(sys.stdin.readline())
test = []
total = ''
for i in range(1, n + 1):
    test.append(i)

while len(test) > 1:
    total += str(test.pop(0)) + ' '
    test.append(test.pop(0))

total += str(test.pop(0))
print(total)