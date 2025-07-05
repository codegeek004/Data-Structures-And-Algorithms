n = int(input())

def odd_nums(n):
    if n>0:
        odd_nums(n-1)
        print(2*n-1, end = ' ')

def even_nums(n):
    if n>0:
        even_nums(n-1)
        print(2*n, end = ' ')

def odd_reverse(n):
    if n>0:
        print(2*n-1, end = ' ')
        odd_reverse(n-1)

def even_reverse(n):
    if n>0:
        print(2*n-1, end = ' ')
        even_reverse(n-1)

def sum_natural_nums(n):
    if n<=1:
        return 1
    return n + sum_natural_nums(n-1)

def sum_odd_nums(n):
    if n<=1:
        return 1
    return 2*n-1 + sum_odd_nums(n-1)

def sum_even_nums(n):
    if n<=1:
        return 2
    return 2*n + sum_even_nums(n-1)

def factorial(n):
    if n<=1:
        return 1
    return n * factorial(n-1)

def sum_sqaures(n):
    if n<=1:
        return 0
    return n*n + sum_sqaures(n-1)

odd_nums(n)
print()
odd_reverse(n)
print()
even_nums(n)
print()
even_reverse(n)
print()
print(sum_natural_nums(n))
print(sum_odd_nums(n))
print(sum_even_nums(n))
print(factorial(n))
print(sum_sqaures(n))
