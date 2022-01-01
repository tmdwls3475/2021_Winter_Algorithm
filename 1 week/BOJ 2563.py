n = int(input())
total = n * 100
l = []

if n <= 100:
    for _ in range(n):
        r = input().split()
        if (int(r[0]) <= 90 and int(r[1]) <= 90):
            d1 = int(r[0])
            d2 = int(r[1])
            l.append((d1, d2))

for i in range(n - 1):
    for j in range(i + 1, n):
        width = 0
        height = 0
        if abs(l[i][0] - l[j][0]) < 10:
            if l[i][0] > l[j][0]:
                width = abs(l[j][0] + 10 - l[i][0])
            else:
                width = abs(l[i][0] + 10 - l[j][0])
        if abs(l[i][1] - l[j][1]) < 10:
            if l[i][1] > l[j][1]:
                height = abs(l[j][1] + 10 - l[i][1])
            else:
                height = abs(l[i][1] + 10 - l[j][1])
        print(width * height)
        total -= (width * height)

print(total)
