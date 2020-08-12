import sys

point = list(input())
dx = [2, 2, -2, -2, 1, -1, 1, -1]  # 알파벳, 열 a
dy = [1, -1, 1, -1, 2, 2, -2, -2]  # 숫자, 행 1

count = 0

for i in range(8):
    if 104 >= ord(point[0]) + dx[i] >= 97 and 8 >= int(point[1]) + dy[i] >= 1:
        count += 1
    else:
        continue

print(count)
