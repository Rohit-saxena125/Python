# count b word in the string
word = input('Enter the word :')
small_letter , capital_letter = input().split()
count = 0
Count =0
for b in word :
    if b == small_letter :
        count += 1
    elif b == capital_letter :
        Count += 1
else :
    print('number of small word  = ',count)
    print('number of capital word  = ', Count)