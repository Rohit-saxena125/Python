'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
n = int(input("Enter the number of lines :"))
k = n - 1
for i in range(0,n):
    for j in range(0,k):
        print(end=' ')
    k -=1
    for i in range(0,i+1):
        print('* ',end='')
    print('\r')
