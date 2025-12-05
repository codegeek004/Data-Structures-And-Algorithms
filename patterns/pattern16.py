'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

n = int(input())
spaces = (n-1)*2
stars = 1
for i in range(n):
    print('*'*stars + ' '*spaces + '*'*stars)
    spaces-=2
    stars+=1

spaces = 2
stars = n-1
for j in range(n):
    print('*'*stars + ' '*spaces + '*'*stars)
    spaces+=2
    stars-=1





