import sys

num = int(sys.stdin.readline().rstrip())  # 식량 개수
food = list(map(int, sys.stdin.readline().rstrip().split()))  # 식량 창고
d = [0] * 1000

d[0] = food[0]
d[1] = max(food[0], food[1])

for i in range(2, num):  # 인덱스를 고려하기 위해 num까지로 설정해야 함
    d[i] = max(d[i - 1], d[i - 2] + food[i])

print(d[num - 1])  # 4개를 넣어도 궁금한 건 d[3]이기 때문에 num-1
