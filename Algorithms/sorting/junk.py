def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert = i
        temp = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > temp:
                arr[j+1] = arr[j]
                insert = j
            else:
                break
        arr[insert] = temp
    return arr

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        minval = i
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                minval = j
        arr[i], arr[minval] = arr[minval], arr[i]
    return arr

def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
    return arr


arr = [1,9,12,7,3,98]

print(insertion_sort(arr))
print(selection_sort(arr))
print(bubble_sort(arr))
