# display the reverse of the number entered using while loop
num = int(input("Enter the number :"))
x = num
rev = 0
while num>0:
    rem = num % 10
    num //= 10
    rev = rev*10 + rem
print("Reverse of a entered number ",x,"=",rev)