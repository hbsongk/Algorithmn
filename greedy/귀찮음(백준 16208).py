import sys

def input():
    return sys.stdin.readline().rstrip()
    
N = int(input())
arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append((x,y))
arr.sort(key = lambda x : (x[1], x[0]))

end_time = arr[0][1]
ans = 1

for i in range(1, len(arr)):
    if arr[i][0] >= end_time:
        end_time = arr[i][1]
        ans += 1
print(ans)
