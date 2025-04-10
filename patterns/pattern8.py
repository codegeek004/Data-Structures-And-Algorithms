"""
9
87
654
3210
"""

n = int(input("Enter the value: "))
for i in range(n):
    for j in range(i):
        if n>=0:
            print(n, end="")
            n-=1
    print()

