def linear_search(arr, search_Element):
    left = 0
    length = len(arr)
    position = -1
    right = length - 1

    for left in range(0, right // 2 + 1, 1):
        if (arr[left] == search_Element):
            position = left
            print(position + 1,"번째", left + 1, " Attempt")
            break

        if (arr[right] == search_Element):
            position = right
            print(position + 1,"번째", length - right, " Attempt")
            break
        
        left += 1
        right -= 1

    if (position == -1):
        print("Not found in Array with ", left, " Attempt")

# drive code

arr = [3,6,9,12,15]
search_element = 15
linear_search(arr, search_element)
