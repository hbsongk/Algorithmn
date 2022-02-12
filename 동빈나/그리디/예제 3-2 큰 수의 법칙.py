n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[n-1]
second = arr[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = first*count + second*(m-count)
print(result)