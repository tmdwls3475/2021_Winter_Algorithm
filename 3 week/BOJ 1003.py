import sys

def fib(N):
    list = [0, 1]
    for i in range(2, N + 1):
        list.append(list[i - 2] + list[i - 1])
    return list[N - 1], list[N]

n = int(sys.stdin.readline())
str = ''

for _ in range(n):
    N = int(sys.stdin.readline())
    zero, one = fib(N)
    str += f'{zero} {one}\n'
print(str, end = '')