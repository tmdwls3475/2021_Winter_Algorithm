def div(n):
    n_length = len(str(n))
    total = []
    for _ in range(n_length):
        total.append(str(n % 10))
        n = n // 10
    return total

n = int(input())
div_list = div(n)
print(div_list)
div_len = len(div_list)

for i in range(div_len):
    if div_list[i] == '0':
        continue
