'''
A
B B
C C C
D D D D
E E E E E
'''
n = int(input("Enter the number of lines:"))
num = 65
for i in range(n):
    for j in range(i+1):
        print(chr(num),end=' ')
    num += 1
    print()