for i in range(2,-1,-1):
    password = input("Enter the password:")
    if password == 'Python':
        print('Welcome to python programming!!')
        break
    else :
        print("sorry you are entered wrong password",i,'attemts are left please try again')
exit()