# Traverse all element using for loop
s = input('Enter the string :')
for ch in s :
    print(ch,end ='')
print('\n',max(s),min(s),len(s))
print('---------------------------------------------------------------------------------------------------------------')
s = input('Enter the string :')
for ch in range(0,len(s),2) :
    print(s[ch],end =' ')
print('\n',max(s),min(s),len(s))
print('################################################################################################################')
s = input('Enter the string :')
index = 0
while index < len(s):
    print(s[index], end=' ')
    index +=1