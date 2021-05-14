# user given position find character
word = input('Enter the string :')
position= int(input())
counter = 0
for i in word :
   if counter == position:
        print('charcter at position',position,'=',i)
   counter += 1