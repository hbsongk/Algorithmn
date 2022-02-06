import sys

N, M = map(int, input().split())
choose = [0 for _ in range(10)]

def dfs(depth):
    if depth == M:
        for idx in range(M):
            print(choose[idx], end = " ")
        print()
        return
    for i in range(1, N+1):
        choose[depth] = i
        dfs(depth + 1)

dfs(0)