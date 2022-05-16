import sys


N = int(input())
ilst = [int(sys.stdin.readline()) for _ in range(N)]

answer = []

def q_sort(lst):
    
    pivot = lst[0]
    left = []
    right = []
    for i in range(len(lst)):
        if lst[i] < pivot:
            left.append(lst[i])
        elif lst[i] > pivot:
            right.append(lst[i])
        else:
            continue
    