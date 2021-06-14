from operator import itemgetter
import Input_dict as dicto
lis = dicto.list_dict_2d(int(input()),int(input()))
# using sorted and itemgetter to print list sorted by age
print(sorted(lis,key=itemgetter("age")))
# using sorted and itemgetter to print list sorted by age and name
print(sorted(lis,key=itemgetter('age','name')))
# using sorted and itemgetter to print list sorted by age in descending order
print(sorted(lis,key=itemgetter("age"),reverse=True))
# using lambda fuction
# using sorting to print list sorted by age
print(sorted(lis, key=lambda i : i['age']))
# using sorting to print list sorted by age and name
print(sorted(lis, key=lambda i : (i['age'],i['name'])))
# using sorting to print list sorted by age in descending order
print(sorted(lis, key=lambda i : i['age'], reverse=True))
