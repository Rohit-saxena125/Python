# convert list of list into dictionary
s = ' using loop  '
print(s.center(len(s)+20,'*'))
list1 = [['a','b',1,2],['c','d',3,4],['e','f',5,6]]
result = dict()
for i in list1:
    result[tuple(i[:2])]  = tuple(i[2:])
print(result)
s = ' dictionary comprehension '
print(s.center(len(s)+20,'*'))
result = {tuple(i[:2]) : tuple(i[2:]) for i in list1}
print(result)