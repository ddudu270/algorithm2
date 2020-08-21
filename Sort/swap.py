N, K = map(int, input().split())  # 자연수 개수, 최대 교환 횟수

A = list(map(int, input().split()))  # 우리가 도와야 하는 배열
B = list(map(int, input().split()))

A.sort()  # 오름차순
B = sorted(B, reverse=True)  # 내림차순

for i in range(K):
    if A[i] >= B[i]:
        break
    else:
        A[i], B[i] = B[i], A[i]

print(sum(A))
