# wap to create a list 'A' to generates squares of a number from (1 to 10) , list 'B' to generates cubes of a number from (1 to 10)
# and list 'C' with those elements that are even and present in list 'A'.
num = int(input())
A = [x**2 for x in range(num)]
print(A)
B = [x**3 for x in range(num)]
print(B)
C = [x for x in A if x % 2 == 0]
print(C)