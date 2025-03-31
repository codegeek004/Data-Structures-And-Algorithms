def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [7,4,10,8,3,1]
print(selection_sort(arr))
