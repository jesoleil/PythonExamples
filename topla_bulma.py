
print("Girilen Sayıların Toplamını Bulma")
toplam=0
while True:
    sayi=input("Sayi girin : ")
    if(sayi=="q" or sayi=="Q"):
        print("Çıkış yapıldı..")
        break
    else:
        sayi=int(sayi)
        toplam+=sayi
        print("Toplam : ",toplam)
    