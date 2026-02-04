# iterative approach
# arr = ['a0_', 'a1_', 'a2_', 'a3_', 'a4_', 'a5_', 'a6_']


def expression(arr, x):
    Exp = ['a0']
    temp = x
    n = len(arr)
    for i in range(1, len(arr)):
        j = i
        while j <= i:
            print('j', j)
            temp *= x
            print('temp:', temp)
            j += 1

        print('final temp', temp)
        print(arr[i] + str(temp))
        Exp.append(arr[i] + str(temp))
    str1 = ''
    final_exp = "+".join(Exp)
    return final_exp


# print(expression(arr, 2))

# recursive appraoch

# def recursive(arr, x, temp, i=1, Exp=['a0']):
def recursive(arr, x, temp, i=0, Exp=0):
    if i == len(arr):
        return Exp
    temp *= x
    # Exp.append(arr[i]+str(temp))
    Exp += (temp*arr[i])
    return recursive(arr, x, temp, i+1, Exp)


x = 2
temp = x
arr = [4, 5, 6, 7]
print(recursive(arr, x, temp))
