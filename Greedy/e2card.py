import sys

N, M = map(int, sys.stdin.readline().split())
num_list = [] # 리스트 정의
sum = [] # min 들을 넣어두기

# 입력 받은 수들을 리스트에 넣어 2차원으로 만들기
for i in range(N):
    num_list.append(list(map(int, input().split())))
    sum.append(min(num_list[i]))

print(max(sum))




