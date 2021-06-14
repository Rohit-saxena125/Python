def vowel_count(x):
    count = 0
    vowel = set("aeiouAEIOU")
    for i in x:
        if i in vowel:
            count += 1
    return count
def concat(a,b):
    s1 =set(a)
    s2 = set(b)
    common = list(s1 & s2)
    result = [ch for ch in s1 if ch not in common] + [ch for ch in s2 if ch not in common]
    return ("".join(result))
if __name__ == "__main__":
    print(vowel_count(input()))
    print(concat(input(),input()))