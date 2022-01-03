import sys

card_and_sum = list(map(int, sys.stdin.readline().split()))
card_num = card_and_sum[0]
card_sum_limit = card_and_sum[1]
max = 0

card_list = list(map(int, sys.stdin.readline().split()))

for i in range(card_num - 2):
    for j in range(i + 1, card_num):
        for e in range(j + 1, card_num):
            total = card_list[i] + card_list[j] + card_list[e]
            if max < total <= card_sum_limit:
                max = total
print(max)