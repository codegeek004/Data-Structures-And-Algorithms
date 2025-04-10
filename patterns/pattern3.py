"""
1111
2222
3333
4444
"""

a = int(input("Enter the value: "))

for i in range(0, a+1):
    print(f"{i}"*a, end=" ")
    print()
