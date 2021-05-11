'''
    * * * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
'''
n = int(input("Enter the number of lines :"))
k = n - 1
for i in range(n,-1,-1):
    for j in range(k,0,-1):
        print(end=' ')
    k +=1
    for i in range(0,i+1):
        print('* ',end='')
    print('\r')