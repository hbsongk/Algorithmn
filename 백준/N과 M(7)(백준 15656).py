import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
choose = [0 for _ in range(10)]
arr = sorted(list(map(int, input().split())))

def dfs(depth):
    if depth == M:
        for idx in range(depth):
            print(arr[choose[idx]], end = " ")
        print()
        return
    for i in range(N):
        choose[depth] = i
        dfs(depth + 1)
dfs(0)