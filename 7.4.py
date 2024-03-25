def kata (i):
    temp = i.split()
    Sstr = ""
    Lstr = ""
    for a in range(len(temp)):
        if a == 0:
            Sstr = temp [0]
            Lstr = temp [0]
        else:
            if len(Lstr) < len(temp[a]):
                Lstr = temp [a]
            if len(Sstr) > len(temp[a]):
                Sstr = temp[a]
    print(Lstr)
    print(Sstr)
sentence = input("Masukan kalimat: ")
kata(sentence)