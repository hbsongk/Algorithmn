import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ans = 0
if N == 0:
    print(ans)
else:
    queue = deque(list(map(int, input().split())))
    while queue:
        weight = 0
        while queue and weight + queue[0] <= M:
            weight += queue.popleft()
        ans += 1
    print(ans)

Reference: https://github.com/tony9402/baekjoon/blob/main/solution/greedy/1817/main.py