import sys

num = int(sys.stdin.readline().rstrip())
d = [0] * 30001  # dp 테이블

for i in range(2, num + 1):
    d[i] = d[i - 1] + 1  # 현재의 수에서 1을 빼는 경우
    if i % 2 == 0:  # 2로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[num])
