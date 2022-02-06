import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
choose = []
visited = [0] * 10

def dfs(depth):
    if depth == M:
        for idx in range(M):
            print(choose[idx], end = " ")
        print()
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        choose.append(i)
        dfs(depth + 1)
        visited[i] = 0
        choose.pop()
dfs(0)