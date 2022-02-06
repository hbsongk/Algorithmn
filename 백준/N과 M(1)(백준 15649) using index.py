import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
choose = [0 for _ in range(10)]
used = [0] * 10

def dfs(depth):
    if depth == M:
        for idx in range(M):
            print(choose[idx], end = " ")
        print()
        return
    for i in range(1, N+1):
        if used[i]:
            continue
        used[i] = 1
        choose[depth] = i
        dfs(depth + 1)
        used[i] = 0
dfs(0)