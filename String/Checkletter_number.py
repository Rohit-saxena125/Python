def check(str1):
    flag1 = False
    flag2 = False
    for i in str1 :
        if i.isalpha():
            flag1 = True
        if i.isdigit():
            flag2 = True
    return flag1 and flag2
print(check(input()))