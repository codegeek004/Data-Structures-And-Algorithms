def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        temp = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > temp:
                #right shifts the elements 
                arr[j+1] = arr[j]
                #updates insert position
                insert_index = j
            else:
                break
        #inserts data based on updated insert position
        arr[insert_index] = temp
 
    return arr
arr = [5,4,10,1,6,2]
print(arr)
print(insertion_sort(arr))
