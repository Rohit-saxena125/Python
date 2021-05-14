# Eliminate letter in a string
word , letter = input('Enter the string  :'),input('removing letter:')
newstr = ''
newstr = word.replace(letter,'')
print('The string is = {0} removing letter {1} new string is = {2}'.format(word,letter,newstr))
