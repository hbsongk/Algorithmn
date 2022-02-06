import sys

N, M = map(int, input().split())
used = [0 for _ in range(10)]
choose = [0 for _ in range(10)]

def dfs(depth, i):
    if depth == M:
        for idx in range(M):
            print(choose[idx], end = " ")
        print()
        return
    for i in range(i, N+1):
        if used[i]:
            continue
        used[i] = 1
        choose[depth] = i
        dfs(depth + 1, i + 1)
        used[i] = 0

dfs(0, 1)