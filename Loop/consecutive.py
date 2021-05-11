# add consecutive numbers using while loop
a = int(input("Enter the number :"))
count = 0
sum = 0
while count <= a:
    sum += count
    count +=1
print("the sum of first",a,'numbers =',sum)