import sys

def input():
    return sys.stdin.readline().rstrip()

S = int(input())
answer = 0
left = 1
right = S

while left <= right:
    mid = (left + right) // 2

    if mid*(mid+1) // 2 <= S:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)