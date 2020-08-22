import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
# N은 떡의 개수 M은 요청한 떡 길이
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
# count = 0  # 최종 결과
# H = 1
#
# while True:
#     for i in num_list:
#         if i <= H:
#             continue
#         else:
#             count += (i-H)
#     if count < M:
#         print(H)
#         break
#     H += 1

start = 0
end = max(num_list)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in num_list:
        if i > mid:
            total += i - mid
    if total < M:
        end = mid - 1
    else:  # total >= M
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로
        start = mid + 1

print(result)
