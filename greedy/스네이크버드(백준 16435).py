import sys

def input():
    return sys.stdin.readline().rstrip()

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in arr:
    if L >= i:
        L += 1
print(L)

Reference: https://github.com/tony9402/baekjoon/blob/main/solution/greedy/16435/main.py