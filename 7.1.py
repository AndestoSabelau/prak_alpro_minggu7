def anagram (a,b):
    if sorted (a) == sorted (b):
        print(True)
    else:
        print(False)

str1 = input("Masukan Kata Pertama: ")
str2 = input("Masukan Kata Kedua: ")
anagram(str1,str2)