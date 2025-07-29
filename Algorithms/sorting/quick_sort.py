def quick_sort(A, low, high):
    if low<high:
        partition_point = partition(A, low, high)
        quick_sort(A, low, partition_point-1)
        quick_sort(A, partition_point+1, high)

def partition(A, low, high):
    pivot = A[low]
    left = low+1
    right = high
    done = False
    while not done:
        while left<= right and A[left]<=pivot:
            left+=1
        while A[right]>=pivot and right>=left:
            right-=1

        #if right<left:
        if left>right:
            done=True
        else:
            #temp = A[left]
            #A[left] = A[right]
            #A[right] = temp
            A[left], A[right] = A[right], A[left]

    #temp = A[low]
    #A[low] = A[right]
    #A[right] = temp
    A[low],A[right] = A[right], A[low]
    return right


A = [50,25,92,16,76,30,43,54,19]
quick_sort(A, 0, len(A)-1)
print(A)

