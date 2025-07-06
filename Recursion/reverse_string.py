def reverse_str(str1, new_str, last_index):
    if last_index < 0:
        return new_str
    new_str += str1[last_index]
    return reverse_str(str1, new_str, last_index-1)

str1 = "lord pulkit"
new_str = ''
print(reverse_str(str1,new_str, len(str1)-1))

