import sys


def bin(x, start, end): # m에 해당하는 물건이 있는지 확인하는 함수
    if start > end:
        return 'no'
    mid = (start+end) // 2
    if n_list[mid] == x:
        return 'yes'
    elif n_list[mid] > x:
        return bin(x, start, mid-1)
    else:
        return bin(x, mid+1, end)


n = int(sys.stdin.readline().rstrip())  # 우리가 가진 물건 개수
n_list = list(map(int, sys.stdin.readline().rstrip().split()))
n_list.sort()

m = int(sys.stdin.readline().rstrip())  # 찾아야 하는 물건 개수
m_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in m_list:
    print(bin(i, 0, n-1), end=' ')
