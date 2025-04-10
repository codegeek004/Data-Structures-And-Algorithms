"""
1
23
456
78910
"""

n = int(input("Enter the value: "))
num = 1

for i in range(n):
    for j in range(i):
        print(num, end= '')
        num+=1
    print()

