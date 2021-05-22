# find the positive integer and negative integer in a list or in a range or count
list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
print('positive_negative in a list :')
pos = []
neg = []
for i in list1:
    if i >=0:
        pos.append(i)
    else :
        neg.append(i)
print('positive list:',pos,'\nNegative list:',neg)
print('positve_negative in a range :')
pos = []
neg = []
for i in range(int(input('Enter the range starting:')),int(input('Enter the range ending:'))):
    if i >0:
       pos.append(i)
    else :
        neg.append(i)
print('positive list:',pos,'\nNegative list:',neg)
print('positive_negative count  :')
print('count of positive list :',len(pos))
print('count of negative list :',len(neg))