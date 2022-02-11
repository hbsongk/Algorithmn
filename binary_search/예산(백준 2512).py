import sys

def input():
    return sys.stdin.readline().rstrip()

def binary_search():
    start, end = 0, max(arr)

    while start <= end:
        mid = (start + end) // 2
        total_budget = 0
        for i in arr:
            if i < mid:
                total_budget += i
            else:
                total_budget += mid
        if total_budget <= M:
            start = mid + 1
        else:
            end = mid - 1
    return end
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
print(binary_search())