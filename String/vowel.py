# count vowel a,e,i,o,u
s1  = 'Lower case vowel'
s1.centre(30,'*')
word = input('Enter the string :')
for v in 'aeiou' :
    print(v ,':',word.count(v))

s = 'Upper case vowel'
s.centre(30,'*')