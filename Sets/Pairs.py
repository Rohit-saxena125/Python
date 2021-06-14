def complete_pair(set1,set2):
    count = 0
    for i in set1 :
        for j in set2 :
            result = i + j
            set3 = set([ch for ch in result if ord(ch) >= ord("a") and ord(ch) <= ord("z")])
            if len(set3) == 26 :
                count += 1
    return count
def list_input_1d(n):
    list1 = []
    for i in range(n):
        a = input()
        list1.append(a)
    return list1
if __name__ == '__main__':
    set1 = list_input_1d(4)
    set2 = list_input_1d(3)
    print(complete_pair(set1,set2))