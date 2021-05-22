# find whether the number is prime or not
def prime(num):
    for b in range(2, num + 1):
        if b > 1:
            for i in range(2, b):
                if b % i == 0:
                    break
            else:
                print(b)
prime(int(input()))
