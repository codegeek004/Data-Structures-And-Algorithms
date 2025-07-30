def binary_search(A, val, low=0, high=-1):
    if not A:
        return -1
    if high == -1:
        high = len(A)-1
    if low == high:
        if A[low]==val:
            return low
        else:
            return -1
    mid = low+(high-low)//2
    if A[mid]>val:
        return binary_search(A, val, low, mid-1)
    elif A[mid]>val:
        return binary_search(A, val, mid+1, high)
    else:
        return mid
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
A.sort()
print(binary_search(A, 535))
