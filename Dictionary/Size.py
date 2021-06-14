import Input_dict as dicto
if __name__ == "__main__":
    d1 = dicto.dictionary_input_1d(int(input("Enter the size of dictionary")))
    d2 = dicto.dictionary_input_1d(int(input("Enter the size of dictionary")))
    d3 = dicto.dictionary_input_1d(int(input("Enter the size of dictionary")))
    print(f"{d1.__sizeof__()}bytes")
    print(f"{d2.__sizeof__()}bytes")
    print(f"{d3.__sizeof__()}bytes")