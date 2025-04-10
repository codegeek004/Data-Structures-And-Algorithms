"""
    *
   ***
  *****
 *******
  *****
   ***
    *
"""

n = int(input("Enter the value: "))
x = 1
for i in range(1, n+1):
    print(" "*(n-i) + "*"*x)
    x+=2
x-=4
for j in range(1, n):
    print(" "*j + "*"*x)
    x-=2 
   
   

