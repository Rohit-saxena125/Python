'''
A
B C
D E F
G H I J
K L M N O
'''
n = int(input("Enter the number of lines:"))
num = 65
for i in range(n):
    for j in range(i+1):
        print(chr(num),end=' ')
        num += 1
    print()