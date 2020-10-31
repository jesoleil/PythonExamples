print("Armstrong Sayılar")
sayi=input("Bir sayı giriniz : ")
basamak_sayisi=len(sayi)
sayi=int(sayi)
basamak=0
toplam=0
gecici=sayi
while(gecici>0):
    basamak=gecici%10
    toplam+=basamak**basamak_sayisi
    gecici//=10

if(toplam==sayi):
    print("Girilen sayı bir Armstrong sayıdır..")
else:
    print("Giririlen sayı Armstrong sayı değildir..")