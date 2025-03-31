def InsertionSort(arr):
    for i in range(1,len(arr)):
        insert_position = i
        temp = arr[i]
        print('temp', temp)
        for j in range(i-1, -1, -1):
            if arr[j] > temp:
                arr[j+1] = arr[j]
                print('right shifting', arr)
                insert_position = j
            else:
                break
        arr[insert_position] = temp
        print('after insertion', arr, '\n')
    return arr
arr = [4,8,3,7,1,19]
print(arr)
print(InsertionSort(arr))
