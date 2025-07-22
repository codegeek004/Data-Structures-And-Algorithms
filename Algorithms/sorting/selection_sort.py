def selection_sort(a):
    
    for i in range(len(a)-1, 0, -1):
        largest = 0
        for j in range(1,i+1):
            if a[j] > a[largest]:
                largest = j
        a[largest], a[j] = a[j], a[largest]
a = [4,5,10,43,57,91,45,9,7]
selection_sort(a)
print(a)

