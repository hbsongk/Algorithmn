def linear_search(arr, n, x):
    for i in range(n):
        if(arr[i] == x):
            return i
    return -1

# driver code

arr = [10,11,12,13,14,15,16,17,18,19]
n = len(arr)
x = 15

# function call

result = linear_search(arr, n, x)
if result == -1:
    print("Element is not present")
else:
    print("Element is present in index",result)