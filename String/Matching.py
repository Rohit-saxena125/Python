def count(str1,str2) :
    set1 = set(str1)
    set2 = set(str2)
    matched = set1 & set2
    print(len(matched))
def count1(str1,str2):
    c,j = 0,0
    for i in str1 :
        if str2.find(i) >= 0 and j == str1.find(i) :
            c += 1
        j += 1
    print(c)
s = input()
s1 = input()
count(s,s1)
count1(s,s1)
