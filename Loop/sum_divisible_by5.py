#sum of the number who divisible by 5 using while loop
count = int(input("Enter the starting number :"))
end = int(input("Enter the end number :"))
sum = 0
while count <= end:
    if count % 5 ==0:
        sum += count
    count += 1
print("The sum of numbers from",count,'to',end,'divisible by 5=',sum)