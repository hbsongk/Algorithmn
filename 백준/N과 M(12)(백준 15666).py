import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
choose = [0 for _ in range(10)]

def dfs(cnt, i):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(arr[choose[idx]], end = " ")
        print()
        return
    pre = -1
    for i in range(i, N):
        if pre == arr[i]:
            continue
        pre = arr[i]
        choose[cnt] = i
        dfs(cnt + 1, i)

dfs(0, 0)