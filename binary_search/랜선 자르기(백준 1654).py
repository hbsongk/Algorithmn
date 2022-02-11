import sys

def input():
    return sys.stdin.readline().rstrip()

def binary_search():
    global ans
    start, end = 1, max(arr)

    while start <= end:
        mid = (start + end) // 2
        total_length = 0
        for i in arr:
                total_length += i // mid
        if total_length < M:
            end = mid - 1
        else:
            start = mid + 1
    ans = end

N, M = map(int, input().split())
arr = []
ans = 0

for i in range(N):
    arr.append(int(input()))
binary_search()
print(ans)