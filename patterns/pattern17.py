"""
A
AB
ABC
ABCD
ABCDE
"""

alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()

n = int(input())
for i in range(n):
    for j in range(i):
        print(alphabets[j], end='')
    print()





