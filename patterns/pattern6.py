"""
n = 4
****
***
**
*
"""

n = int(input("Enter the value: "))

for i in range(n):
    print("*"*n, end=" ")
    n -= 1
    print()
