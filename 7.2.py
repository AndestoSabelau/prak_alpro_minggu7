def hitung(Sentence,Word):
    Sentence = Sentence.lower()
    Amount = Sentence.count(Word)
    return Amount
Sentence = "Saya mau makan. Makan itu wajib. mau saing atau malam saya wajib makan"
print(hitung(Sentence,"makan"))