def devmod(a, b):
    c = a // b
    d = a % b
    t =(c,d)
    return t
num1 = input()
num2 = input()
print(devmod(int(num1),int(num2)))
