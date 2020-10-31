print("Geometrik şeklin tipini bulma : \nDörtgen\nÜçgen")
tip=input("Hangi geometrik şeklin tipini bulmak istiyorsunuz : ")
if(tip=="Dörtgen" or tip=="dörtgen"):
    a = int(input("1.kenar : "))
    b = int(input("2.kenar : "))
    c = int(input("3.kenar : "))
    d = int(input("4.kenar : "))
    if(a==b and b==c and c==d ) :
        print("KARE")
    elif ((a==b and c==d and a!=c) or (a==c and b==d and a!=b) or (a==d and b==c and a!=b)) :
        print("DİKDÖRTGEN")
    else :
        print("SIRADAN DÖRTGEN")

elif (tip == "Ücgen" or tip == "üçgen"):
    a = int(input("1.Kenar : "))
    b = int(input("2.Kenar : "))
    c = int(input("3.Kenar : "))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("EŞKENAR ÜÇGEN")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İKİZKENAR ÜÇGEN")
        else:
            print("ÇEŞİTKENAR ÜÇGEN")
    else:
        print("Üçgen belirtmiyor !!!!!!")
else :
    print("Geçersiz işlem !!!!!!!!!")
