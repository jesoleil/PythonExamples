import math
def hesapla(sayi):

    if(secim=="1"):
        print("Kosinüs : ",math.cos(sayi))
    elif(secim=="2"):
        print("Sinüs : ", math.sin(sayi))
    elif(secim=="3"):
        print("Tanjant : ", math.tan(sayi))
    elif(secim=="4"):
        print("Kotanjant : ",math.cot(sayi))
    elif(secim=="5"):
        print("Faktöriyel : ",math.factorial(sayi))
    elif(secim=="6"):
        print("Kendinden küçük en büyük sayı : ",math.floor(sayi))
    elif(secim=="7"):
        print("Kendinden büyük en küçük sayı : ",math.ceil(sayi))
    elif(secim=="8"):
        print("10 tabanındaki logaritma : ",math.log10(sayi))
    else:
        print("Yanlış tuş !!")


print("HESAP MAKİNESİ")
print("Programdan çıkmak için q ya da Q ya basınız..")
print("Bir sayının kosinüsü için 1 e \nBir sayının sinüsü için 2 ye\nBir sayının tanjantı için 3 e\nBir sayının kotanjantı için 4 e\nBir sayının faktöriyeli için 5 e\nBir sayıyı kendinden küçük en büyük sayıya yuvarlamak için 6 ya\nBir sayıyı kendinden büyük en küçük sayıya yuvarlamak için 7 ye\nBir sayının 10 tabanındaki logaritması için 8 e basınız..")


while True:
        secim = input("Seçiminiz : ")
        if(secim=="q" or secim=="Q"):
            print("Programdan çıkıldı..")
            break

        else:
            sayi=float(input("Sayınız: "))
            hesapla(sayi)





