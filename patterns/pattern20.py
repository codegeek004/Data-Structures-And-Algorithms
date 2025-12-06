"""
   A
  ABA
 ABCBA
ABCDCBA
"""

alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()
n = int(input())
spaces = n-1
for i in range(n):
    print(' '*spaces, end='')
    for j in range(i):
        print(alphabets[j], end='')
    for k in range(i, -1, -1):
        print(alphabets[k], end='')
    spaces-=1
    print()

    





