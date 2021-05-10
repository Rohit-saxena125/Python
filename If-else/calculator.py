num1,num2 =eval(input("Enter the number:"))
print("1) Addition\n2) Subtraction\n3)Multiplication\n4)Division")
choice = int(input("Enter the choice:"))
if choice == 1 :
    print("Addition of",num1,'and',num2,'is:',num1+num2)
elif choice == 2 :
    print("Subtraction of",num1,'and',num2,'is:',num1-num2)
elif choice == 3 :
    print("Multiplication of",num1,'and',num2,'is:',num1*num2)
elif choice == 4 :
    print("Division of",num1,'and',num2,'is:',num1/num2)
else :
    print("Soory you entered invalid choice")
