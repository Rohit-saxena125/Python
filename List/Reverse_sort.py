# Reverse row sort in list of list

list1 = []
for i in range(int(input())):
    a  =list(map(int,input().split()))
    list1.append(a)
s = 'using loop + sort + reverse'
print(s.center(len(s)+ 20,'*'))
for i in list1:
    i.sort(reverse= True)
print(list1)
s = 'using list comprehension'
print(s.center(len(s)+ 20,'*'))
list1 = [sorted(i,reverse= True) for i in list1]
print(list1)