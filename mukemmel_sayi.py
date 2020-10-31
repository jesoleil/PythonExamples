sayac = 1
toplam = 0

sayi = int(input("Bir sayı giriniz : "))

while(sayac < sayi):
    if(sayi % sayac == 0):
        toplam += sayac
    sayac += 1

if (sayi == toplam):
    print("{} sayısı mükemmel sayıdır..".format(sayi))

else :
    print("{} sayısı mükemmel sayı değildir..".format(sayi))
