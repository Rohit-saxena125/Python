# Eliminate letter in a string
word , letter = input('Enter the string  :'),input('removing letter:')
s = ' using str.replace() '
newstr = ''
print(s.center(len(s)+20,'*'))
newstr = word.replace(letter,'') #remove all occurance
print('The string is = {0} removing letter {1} new string is = {2}'.format(word,letter,newstr))
newstr = word.replace(letter,'',1) # remove first occurance
print('The string is = {0} removing letter {1} new string is = {2}'.format(word,letter,newstr))
s = ' using native '
print(s.center(len(s)+20,'*'))
for i in range(len(word)):
    if i != letter:
        newstr += word[i]
print('The string is = {0} removing letter {1} new string is = {2}'.format(word,letter,newstr))
s = ' using slice + concatenation '
print(s.center(len(s)+20,'*'))
# removing character at position
n = int(input('enter removing position :'))
newstr = word[ :n] +word[n+1:]
print(newstr)
s = ' using str.join() + list comprehension '
print(s.center(len(s)+20,'*'))
newstr = ''.join([word[i] for i in range(len(word)) if i != letter])
print('The string is = {0} removing letter {1} new string is = {2}'.format(word,letter,newstr))
