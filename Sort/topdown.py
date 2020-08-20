N = int(input())
num_list = [int(input()) for j in range(N)]

num_list.sort()
num_list.reverse()
# num_list = sorted(num_list, reverse=True)

for i in num_list:
    print(i, end=' ')
