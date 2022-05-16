import sys


N = int(input())
lst = [int(sys.stdin.readline()) for _ in range(N)]

sort = sorted(lst)
for y in sort:
    print(y)
