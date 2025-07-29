# time complexity --> O(n)
# space complexity --> O(n)
#unordered linear search
def unordered_linear_search(list1, val):
    for i in range(len(list1)):
        if list1[i] == val:
            return i
    return -1 
list1 = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(unordered_linear_search(list1, 565))

#sorted/ordered linear search. if the array is sorted then we dont need to scan the whole array

def ordered_linear_search(list1, val):
    for i in range(len(list1)):
        if list1[i] == val:
            return i
        elif list1[i]>val:
            return -1
    return -1
list1.sort()
print(ordered_linear_search(list1, 321))
