import sys


def eq1(x, y):
    count = 0
    while x != 1:
        if x % y == 0:
            x = int(x / y)
            count += 1
        else:
            x -= 1
            count += 1
    return count


N, K = map(int, sys.stdin.readline().split())
print(eq1(N, K))
