def Palindrome(num):
    for b in range(1, num + 1):
        temp = b
        rev = 0
        while (temp > 0):
            dig = temp % 10
            rev = rev * 10 + dig
            temp = temp // 10
        if b == rev:
            print(rev)
Palindrome(int(input()))

