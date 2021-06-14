s = input()
print(str(s))
half = len(s) // 2
result = ''
for i in range(len(s)):
    if i > half :
        result += s[i].upper() # result = ''.join([s[i].upper() if i > half else s[i] for i in range(len(s))])
    else :
        result += s[i]
print(str(result))
b = "First and last word capital"
print(s.center(20,'*'))
result = ''.join(map(lambda s : s[ : -1] + s[-1].upper(),s.title().split()))
print(result)