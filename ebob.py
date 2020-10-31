
print("Lütfen ebobları alınacak iki sayi giriniz ..")
def ebob(sayi1,sayi2):
    while(sayi1!=sayi2):
        if(sayi1>sayi2):
            sayi1-=sayi2
        else:
            sayi2-=sayi1
    return sayi1

while True:
    sayi1 = input("Sayı 1 :")
    sayi2 = input("Sayı 2 : ")
    if (sayi1=="q" or sayi1=="Q" or sayi2=="q" or sayi2=="Q"):
        print("Program sonlandı...")
        break
    else:
        sayi1=int(sayi1)
        sayi2=int(sayi2)
        print("Ebobları : ", ebob(sayi1, sayi2))

