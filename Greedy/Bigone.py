import sys

N, M, K = map(int, sys.stdin.readline().split())
# N은 배열 크기 M은 숫자가 더해지는 횟수, K는 최대 횟수
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
sum = 0

num_list.sort()

for i in range(1, M + 1):
    if i % (K + 1) == 0:
        sum += num_list[-2]
    else:
        sum += num_list[-1]

print(sum)
