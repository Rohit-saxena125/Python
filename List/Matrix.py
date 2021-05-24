# addition two matrix
a = [[2,5,8],
     [3,6,9],
     [1,4,7]]
b = [[7,4,1],
     [8,5,2],
     [9,6,3]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]

for r in result:
    print(list(r))
