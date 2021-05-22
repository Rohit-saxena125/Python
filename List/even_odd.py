# find even odd  number in a list or in a range and count even or odd number

list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
print('even odd in a list :')
even = []
odd = []
for i in list1:
    if i % 2 ==0:
        even.append(i)
    else :
        odd.append(i)
print('even list:',even,'\nodd list:',odd)
print('even odd in a range :')
even = []
odd = []
for i in range(int(input('Enter the range :'))):
    if i % 2 ==0:
        even.append(i)
    else :
        odd.append(i)
print('even list:',even,'\nodd list:',odd)
print('even odd count :')
print('count of even list :',len(even))
print('count of odd list :',len(odd))