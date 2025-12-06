"""
E
DE
CDE
BCDE
ABCDE
"""

alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()

n = int(input())

for i in range(n-1, -1, -1):
    for j in range(i,n):
        print(alphabets[j], end='')
    print()


