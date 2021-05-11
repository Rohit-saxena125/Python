# if the user entered the number 5 its triangular number (1+2+3+4+5)=15
num = int(input('Entered the number : '))
triangular_number = 0
for i in range(num,0,-1):
    triangular_number += i
print("triangular number =",triangular_number)