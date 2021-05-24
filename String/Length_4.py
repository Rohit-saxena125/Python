# find length of string 4 ways
word = input()
print('************************* len *********************')
print(len(word))
print('************************* count method *********************')
counter = 0
for i in word :
    counter += 1
print(counter)
print('************************* slicing *********************')
counter = 0
while word[counter :]:
    counter += 1
print(counter)
