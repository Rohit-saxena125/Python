def Armstrong(num):
    for b in range(1, num + 1):
        order = len(str(b))
        sum = 0
        temp = b
        while temp > 0:
            d = temp % 10
            sum += d ** order
            temp //= 10
        if b == sum:
            print(b)
Armstrong(int(input()))
