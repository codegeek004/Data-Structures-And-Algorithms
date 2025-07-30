def binary_search(A, val):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low+high)//2
        if A[mid]>val: 
            high = mid-1
        elif A[mid]<val: 
            low=mid+1
        else: 
            return mid
    return -1
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(binary_search(A, 220))
