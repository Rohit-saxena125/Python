def average(array):
    a = list(set(array))
    s = len(a)
    set1 = sum(a)/s
    return set1
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)