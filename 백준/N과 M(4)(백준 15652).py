import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
choose = [0 for _ in range(10)]

def dfs(depth, i):
    if depth == M:
        for idx in range(depth):
            print(choose[idx], end = " ")
        print()
        return
    for i in range(i, N+1):
        choose[depth] = i
        dfs(depth + 1, i)

dfs(0, 1)