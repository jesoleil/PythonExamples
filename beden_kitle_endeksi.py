print("BEDEN KİTLE ENDEKSİ HESAPLAMA")

boy=float(input("Lütfen boyunuzu giriniz (m) : "))
kilo=float(input("Lütfen kilonuzu giriniz (kg) : "))
bki=kilo/(boy*boy)
if (bki<18.5) :
    print("Zayıf")
elif (bki>=18.5 and bki<25) :
    print("Normal")
elif (bki>=25 and bki<30) :
    print("Fazla Kilolu")
else :
    print("Obez")