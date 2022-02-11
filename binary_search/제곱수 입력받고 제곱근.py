import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

answer = 0
left = 0
right = N

while left <= right:
    mid = (left + right) // 2
    if mid ** 2 <= N:
        answer = mid
        left = mid + 1
    else:
        right =  mid - 1

print(answer)