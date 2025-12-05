"""
1--------1
12------21
123----321
1234--4321
1234554321
"""
n = int(input())
spaces = (n-2)*2

for i in range(1,n):
    for j in range(1,i+1):
        print(j,end='')
    print(' '*spaces, end='')

    for k in range(i, 0, -1):
        print(k,end='')
    spaces-=2
    print()
    
