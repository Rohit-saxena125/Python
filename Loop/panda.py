bar=int(input())
lis=input().split()
lis=list(map(int,lis))
start,Max=bar,0
for i in range(bar):
    if lis[i]==1:
        start=i
        break
p=range(bar)
for i in p[bar-1::-1]:
    if lis[i]==1:
        Max=i
        break
count=0
for i in range(start,Max-1):
    if lis[i]==1:
        if lis[i+1]!=1:
            count+=1
    else :
        count+=1
print(count+1)