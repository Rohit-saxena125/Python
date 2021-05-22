l = []
for i in range(int(input('Enter range  of list'))):
    a = input()
    l.append(a)
b = input('Enter the check word / number:')
if b in l:
    print('element {} is exists'.format(b))
else:
    print('element {} is not exists'.format(b))