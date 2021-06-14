def list_input_1d(n):
    list1 = []
    for i in range(n):
        a = int(input())
        list1.append(a)
    return list1
def add_missing(x,y):
    return set(x).difference(set(y))

if __name__ == "__main__":
    a = list_input_1d(int(input()))
    b = list_input_1d(int(input()))
    print(f"Missing value in list a is {add_missing(a,b)}\nextra value in list a is {add_missing(b,a)}\n")
    print(f"Missing value in list a is {add_missing(b,a)}\nextra value in list a is {add_missing(a,b)}\n")