def div(n):
    n_length = len(str(n))
    total = 0
    for _ in range(n_length - 1):
        total += (n % 10)
        n = n // 10
    total += n
    return total
    
def d(n):
    return n + div(n)

d_list = []

for j in range(1, 9997):
    d_list.append(j)

for i in range(1, 10000):
    d_result = d(i)
    if d_result > 10000:
        break
    if d_result in d_list:
        d_list.remove(d_result)

for i in range(1, len(d_list)):
    print(d_list.pop(0))
