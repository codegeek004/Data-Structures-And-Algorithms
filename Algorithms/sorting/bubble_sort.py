a = [24, 48, 11, 67, 92, 43]
#for i in range(1, len(a)):
#    for j in range(len(a)-i):
#        print(i,j)
#        if a[j] > a[j+1]:
#            a[j], a[j+1] = a[j+1], a[j]
#print(a)


#for i in range(len(a)-1,0, -1):
#    for j in range(i):
#        print(i,j)
#        if a[j] > a[j+1]:
#            a[j], a[j+1] = a[j+1], a[j]
#print(a)

#this takes time complexity O(n) even in best case So we imporove its time complexity by adding flag

#this algorithm imprves the best case complexity O(n)
def bubble_sort(a):
    swapped = 1
    for i in range(len(a)-1, 0, -1):
        if swapped == 0:
            break
        for j in range(i):
            print(i,j)
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = 1
bubble_sort(a)
print(a)
