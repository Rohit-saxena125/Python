# reverse word in a given string
word = input()
words = word.split(' ')
reverse_words = ' '.join(reversed(words))
print(reverse_words)