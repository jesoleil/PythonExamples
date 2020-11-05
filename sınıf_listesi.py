def notHesapla(satir):
    satir=satir[:-1]
    liste=satir.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    genel_not=not1*(0.3)+not2*(0.3)+not3*(0.4)
    if(genel_not>=90):
        harf="AA"
    elif(genel_not>=80):
        harf="BB"
    elif(genel_not>=70):
        harf="CC"
    elif(genel_not>=60):
        harf="DD"
    else:
        harf="FF"
    return isim + "-------->"+harf+"\n"

with open("sinif_listesi.txt","r",encoding="utf-8") as file:
    eklenen_listesi=[]
    for i in file:
        eklenen_listesi.append(notHesapla(i))
    with open("Notlar.txt","w",encoding="utf-8") as file2:
        for i in eklenen_listesi:
            file2.write(i)