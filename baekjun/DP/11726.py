import sys
sys.setrecursionlimit(1000) # 재귀 호출 범위 수정


n = int(input())
mem = [0 for _ in range(1001)]
def tile(n):
    if mem[n] != False:
        return mem[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2

    else:
        mem[n] = (tile(n - 1) + tile(n - 2)) % 10007
        return mem[n]

print(tile(n))