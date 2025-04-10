"""
   *
  ***
 *****
"""
n=int(input("Enter the value:"))
x = 1
for i in range(1, n+1):
    print(" "*(n-i) + "*"*x)
    x+=2
