import sys

n = int(sys.stdin.readline())
test_data_str = ''

for _ in range(n):
    test_data = list(map(int, sys.stdin.readline().split()))
    count = 0
    H = test_data[0]
    W = test_data[1]
    N = test_data[2]
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            count += 1
            if count == N:
                if i < 10:
                    test_data_str += (str(j) + '0' + str(i) + '\n')
                else:
                    test_data_str += (str(j) + str(i) + '\n')
print(test_data_str)