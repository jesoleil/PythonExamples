print("İki Sayıdan Büyük Olanı Bulma")
sayi1=float(input("Birinci sayıyı gir : "))
sayi2=float(input("İkinci sayıyı gir : "))

if (sayi1<sayi2) :
    print("{}, {} dan daha büyüktür".format(sayi2,sayi1))
elif (sayi1==sayi2) :
    print("İki sayı birbirine eşittir..")
else :
    print("{} , {} dan daha büyüktür".format(sayi1,sayi2))