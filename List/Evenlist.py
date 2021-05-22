# show the even number of list
list1 = list(map(int,input('Enter the list :').split()))
print(list1)
list1 = [x for x in list1 if x % 2 == 0]
print(list1)