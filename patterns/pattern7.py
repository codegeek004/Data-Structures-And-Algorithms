"""
4444
333
22
1
"""

n = int(input("Enter the value: "))

for i in range(n):
    print(f"{n}"*n, end=" ")
    n -= 1
    print()
