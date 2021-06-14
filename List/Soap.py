def count(a):
    return a<b
if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        b = int(input())
        c = list(filter(count,a))
        print(len(c))
