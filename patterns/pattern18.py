"""
ABCDE
ABCD
ABC
AB
A
"""

alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()
n = int(input())
for i in range(n-1, -1, -1):
    for j in range(i):
        print(alphabets[j], end='')
    print()

