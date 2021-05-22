'''
Enter the number of values:2
ashi
1 2 3
rohan
2 3 4
rohan
3.00
'''
'''
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
'''
a = int(input("Enter the number of values:"))
my={}
for i in range(a):
    key =input()
    value=list(map(int,input().split()))
    my[key]=value
b=sum(my.get(input()))/3
print(format(b,'.2f'))

s = 'retry'
print(s.center(20,'^'))

a = int(input("Enter the number of values:"))
my={}
for i in range(a):
    a = input()
    dicto = a.split()
    my[dicto[0]] = [int(dicto[1]),int(dicto[2]),int(dicto[3])]
b=sum(my.get(input()))/3
print(format(b,'.2f'))
