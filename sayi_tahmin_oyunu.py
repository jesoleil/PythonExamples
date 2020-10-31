import time
import random

print("Sayı Tahmin Oyununa Hoş Geldiniz..\n 1 ile 40 arasında bir sayı tuttuk, 7 tahmin hakkınız var..")

rastgele_sayi=random.randint(1,40)
tahmin_hakki=7
while True:
    tahmin=int(input("Tahmininiz: "))
    if(tahmin<rastgele_sayi):
        print("Bekleniyor..")
        time.sleep(2)
        print("Daha büyük bir sayı söyleyin..")
        tahmin_hakki-=1
    elif(tahmin>rastgele_sayi):
        print("Bekleniyor..")
        time.sleep(2)
        print("Daha küçük bir sayı söyleyin..")
        tahmin_hakki-=1
    else:
        print("Bekleniyor..")
        time.sleep(2)
        print("Tebrikler !! Sayımız ",rastgele_sayi)
        break
    if(tahmin_hakki==0):
        print("Tahmin hakkınız bitti..")
        print("Sayımız ",rastgele_sayi)
        break