# find frequency of characters in a string
word = input('Enter the string :')
al = {}
for i in word :
    if i in al:
        al[i] += 1
    else :
        al[i] = 1
print(str(al))