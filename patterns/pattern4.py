"""
1
22
333
4444
"""

a = int(input("Enter the value: "))

for i in range(0, a+1):
    print(f"{i}"*i, end=" ")
    print()
