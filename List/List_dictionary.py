# convert list into list of dictionary
s = ' using loop + dictionary comprehension method '
print(s.center(len(s)+20,'*'))
test_list = ['Rohan',3,'is',8,'Best',10,'for',18,'Ashi',33]
key_list = ['name','number']
n = len(test_list)
result = []
for i in range(0,n,2):
    result.append({key_list[0] : test_list[i],key_list[1] : test_list[i+1]})
print(result)
s = ' using list comprehension + dictionary comprehension method '
print(s.center(len(s)+20,'*'))
result = [{key_list[0] : test_list[i],key_list[1] : test_list[i+1]} for i in range(0,n,2)]
print(result)
s = 'my method for user enter'
print(s.center(len(s)+20,'*'))
list1 = []
for i in range(0,int(input('user enter range :'))+1):
    a = input()
    if i % 2 ==0:
        list1.append(a)
    else :
        list1.append(int(a))
key_list = ['name','Age']
n = len(list1)
result = []
for i in range(0,n,2):
    result.append({key_list[0] : list1[i],key_list[1] : list1[i+1]})
print(result)