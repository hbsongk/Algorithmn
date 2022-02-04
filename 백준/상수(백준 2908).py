import sys

def input():
    return sys.stdin.readline().rstrip()

def reverse(x):
    res = 0
    while x > 0:
        remain = x % 10
        res = res * 10 + remain
        x = x // 10
    return res

a, b = map(int, input().split())

if reverse(a) > reverse(b):
    print(reverse(a))
else:
    print(reverse(b))