import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

waiting = 0
total = 0
for i in range(len(arr)):
    waiting += arr[i]
    total += waiting
print(total)