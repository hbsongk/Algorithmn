import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans = []
res = 0
for i in range(N):
    ans.append((arr[i], arr2[i]))
ans.sort(key = lambda x : (x[1], x[0]))
for i in range(N):
    res += ans[i][0] + ans[i][1] * i
print(res)

Reference : gusdn3477(https://github.com/tony9402/baekjoon/blob/main/solution/greedy/14247/main.py)