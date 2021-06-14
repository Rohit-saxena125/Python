def returnSum(d):
    sum = 0
    for i in d :
        sum += d[i]
    return sum
def dictionary_input_1d(n):
    d1 = {}
    for i in range(n):
        a = input().split()
        d1[a[0]] = int(a[1])
    return d1
if __name__ == "__main__":
    print(returnSum(dictionary_input_1d(int(input()))))
