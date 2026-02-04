arr1 = [1, 3, 5, 7, 8, 9]
arr2 = [2, 4, 5, 6, 7, 8]

i = 0
j = 0

while i < len(arr1) or j < len(arr2):
    if arr1[i] <= arr2[j]:
        arr1.insert(i, arr2[j])
    i += 1
    j += 1
