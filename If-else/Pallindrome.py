# check the strin or number is palindrome or not
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string is not a palindrome")


print('====================================number is palindrome or not==========================================')
Num = int(input("Enter a value:"))
Temp = num
Rev = 0
while(num > 0):
    dig = num % 10
    revrev = rev * 10 + dig
    numnum = num // 10
if(temp == rev):
    print("This value is a palindrome number!")
else:
    print("This value is not a palindrome number!")