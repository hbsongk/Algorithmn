import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

total = arr[-1]
for i in range(len(arr) - 1):
    total += arr[i] / 2
print(total)