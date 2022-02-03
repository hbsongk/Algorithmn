arr = []

def d(i):
    ans = str(i)
    total = int(ans)
    for j in ans:
        total = total + int(j)
    arr.append(total)

for i in range(1, 10001):
    d(i)
    if i in set(arr):
        continue
    else:
        print(i)