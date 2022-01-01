import math

d = input().split()
A = int(d[0])
B = int(d[1])
V = int(d[2])

print(math.ceil((V - A) / (A - B) + 1))
# A - B는 알았으나 반복문을 쓰면 안되는 것, 거리가 V - A까지인 것, 나오는 시간에 +1 해주는 것, 그리고 시간 소숫점을 올림해줘야 하는 것은 인터넷 참고함
