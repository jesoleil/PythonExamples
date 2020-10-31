print("****Mükemmel Sayı Bulma****")
def mukemmel_sayi(sayi):
    sayac=1
    toplam=0
    while (sayac < sayi):
        if (sayi % sayac == 0):
            toplam += sayac
        sayac += 1
    return toplam

while True:
    sayi=input("Bir sayi giriniz : ")
    if (sayi=="q" or sayi=="Q"):
        print("Program sonlandı..")
        break
    else :
        sayi=int(sayi)
        if (sayi==mukemmel_sayi(sayi)):
            print(sayi,"mükemmel sayıdır..")
        else:
            print(sayi,"mükemmel sayı değildir..")


