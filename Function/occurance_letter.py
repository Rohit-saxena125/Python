def count_letter(word, letter):
    print('number of occurance',letter,'=',end =' ')
    count = 0
    for i in word :
        if i == letter :
            count += 1
    return count
x = count_letter(input(),input())
print(x)
